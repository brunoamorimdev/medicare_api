from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from user.serializers import UserSerializer
from rest_framework.permissions import AllowAny
from user.models import User
from rest_framework.response import Response


class UserLCView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRUDView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "unique_id"
