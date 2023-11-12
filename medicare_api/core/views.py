from typing import Any
from rest_framework.views import APIView
from rest_framework.response import Response
from core.serializers import BasePaginationFilterSerializer
from core.helpers import CustomPagination, api_view_exception_handler
from authentication.helpers import CustomAuth
from django.contrib.auth.mixins import PermissionRequiredMixin


class BaseAPIView(APIView, PermissionRequiredMixin):
    serializer_filter_class = BasePaginationFilterSerializer
    pagination_class = CustomPagination
    authentication_classes = [CustomAuth]
    raise_exception = True
    permission_required = None

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    def initial(self, request, *args, **kwargs):
        # Request Context
        self.ctx = {
            "method": self.request.method,
            "user": self.request.user,
            "view_name": self.__class__.__name__,
        }

        return super().initial(request, *args, **kwargs)

    def handle_exception(self, exc):
        ctx = self.ctx
        if not ctx:
            ctx = {}
        return api_view_exception_handler(exc=exc, ctx=ctx)

    def get_serialized_query_params(self):
        serializer = self.serializer_filter_class

        if serializer:
            data = getattr(self.request, "query_params")
            serializer = serializer(data=data)
            serializer.is_valid(raise_exception=True)
            return serializer.data
        return {}

    def get_paginated_response(self, serialized_data):
        response = Response(serialized_data)

        pagination = self.get_serialized_query_params().get("pagination", None)
        if pagination == "active":
            # Use your CustomPagination class to paginate the results
            paginator = self.pagination_class()
            response = paginator.get_paginated_response(
                paginator.paginate_queryset(serialized_data, self.request)
            )

        return response
