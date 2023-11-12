import rest_framework.serializers as serializers
from typing import TYPE_CHECKING
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from core.views import BaseAPIView
from core.helpers import ApplicationError
from django.utils.translation import gettext_lazy as _

if TYPE_CHECKING:
    from rest_framework.request import Request


class AuthAPIView(BaseAPIView, ObtainAuthToken):
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
