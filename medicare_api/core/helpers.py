import rest_framework.serializers as serializers
import rest_framework.status as status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from medicare_api.core import settings
from django.core.exceptions import (
    PermissionDenied,
    ObjectDoesNotExist,
)
from django.core.exceptions import ValidationError as DjangoValidationError
from django.http import Http404
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.serializers import as_serializer_error
from rest_framework.views import exception_handler


class ApplicationError(Exception):
    def __init__(
        self: Exception,
        message: str,
        extra={},
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    ):
        super().__init__(message)

        self.status = status
        self.message = message
        self.extra = extra


def clean_msg_exception_if_debug(msg=None):
    if settings.DEBUG and msg is not None:
        return msg
    else:
        return "Ocorreu um erro inesperado."


def api_view_exception_handler(
    exc, ctx={"method": None, "user": None, "view_name": None}
):
    if isinstance(exc, (TypeError, AssertionError, AttributeError, KeyError)):
        exc = exceptions.APIException(exc)

    if isinstance(exc, DjangoValidationError):
        exc = exceptions.ValidationError(as_serializer_error(exc))

    if isinstance(exc, Http404):
        exc = exceptions.NotFound()

    if isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()

    if isinstance(exc, ObjectDoesNotExist):
        exc = exceptions.NotFound()

    response = exception_handler(exc, ctx)

    # If unexpected error occurs (server error, etc.)
    if response is None:
        if isinstance(exc, ApplicationError) or issubclass(exc, ApplicationError):
            data = {
                "status": exc.status,
                "message": clean_msg_exception_if_debug(exc.message),
                "extra": exc.extra,
            }

            return Response(data, status=exc.status)

        data = {
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "message": clean_msg_exception_if_debug(),
            "extra": {},
        }

        return Response(response)

    if isinstance(exc.detail, (list, dict)):
        response.data = {"detail": response.data}

    if isinstance(exc, exceptions.ValidationError):
        response.data["status"] = exc.status_code
        response.data["message"] = "Validation error"
        response.data["extra"] = {"fields": response.data["detail"]}
    else:
        message = response.data["detail"]
        if exc.status_code >= 500:
            message = clean_msg_exception_if_debug(message)
        response.data["status"] = exc.status_code
        response.data["message"] = message
        response.data["extra"] = {}

    del response.data["detail"]

    return response


class CustomPagination(PageNumberPagination):
    page_size = 10  # Set the number of items per page here
    page_size_query_param = "page_size"  # Allow clients to override the page size
    max_page_size = 100  # Set a maximum page size if needed

    def get_next_link(self):
        if not self.page.has_next():
            return None
        page_number = self.page.next_page_number()
        return page_number

    def get_previous_link(self):
        if not self.page.has_previous():
            return None
        page_number = self.page.previous_page_number()
        return page_number

    def get_paginated_response(self, data):
        return Response(
            {
                "count": self.page.paginator.count,
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
                "results": data,
            }
        )


def create_serializer_class(name, fields):
    return type(name, (serializers.Serializer,), fields)


def inline_serializer(*, fields, data=None, **kwargs):
    serializer_class = create_serializer_class(name="inline_serializer", fields=fields)

    if data is not None:
        return serializer_class(data=data, **kwargs)

    return serializer_class(**kwargs)
