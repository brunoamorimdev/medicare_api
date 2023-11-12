import rest_framework.serializers as serializers
from typing import TYPE_CHECKING
from django.utils.translation import gettext_lazy as _
from rest_framework.response import Response
from core.views import BaseAPIView
from core.helpers import ApplicationError
from user.selectors import UserPermissionsSelectors
from rest_framework.permissions import IsAdminUser, IsAuthenticated

if TYPE_CHECKING:
    from rest_framework.request import Request


class AdminPermissionsContentTypesListAPIView(BaseAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    permission_required = "contenttypes.contenttype"

    class OutputSerializer(serializers.Serializer):
        app_label = serializers.CharField()
        model = serializers.CharField()

    def get(self, request: "Request", *args, **kwargs):
        queryset = UserPermissionsSelectors.content_type_list()
        serialized_data = self.OutputSerializer(queryset, many=True).data
        return self.get_paginated_response(serialized_data)


class AdminUsersPermissionsCreateAPIView(BaseAPIView):
    class InputSerializer(serializers.Serializer):
        pass

    class OutputSerializer(serializers.Serializer):
        token = serializers.CharField(source="key")

    def post(self, request: "Request", *args, **kwargs):
        payload = request.data
        if payload:
            token_auth_serializer = self.get_serializer(data=payload)
            token_auth_serializer.is_valid(raise_exception=True)
            user = token_auth_serializer.validated_data["user"]
            token, _ = Token.objects.get_or_create(user=user)
            return Response(self.OutputSerializer(instance=token).data)
        else:
            raise ApplicationError(_("You must provide a username and password."))
