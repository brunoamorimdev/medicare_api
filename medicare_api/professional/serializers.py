import rest_framework.serializers as serializers
from user.models import User
from user.serializers import UserSerializer
from professional.models import Professional, Profession
from rest_framework.request import Request


class ProfessionalSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Professional
        fields = ("unique_id", "profession", "user")

    def get_extra_kwargs(self):
        extra_kwargs = super().get_extra_kwargs()
        request: Request | None = self.context.get("request", None)
        extra_kwargs["profession"] = {"required": False}
        if request is not None and request.method == "POST":
            extra_kwargs["profession"] = {"required": True}
        return extra_kwargs

    def create(self, validated_data):
        user_data = validated_data["user"]
        user_instance = User.objects.create_user(**user_data)
        professional_instance = Professional.objects.create(**validated_data)
        professional_instance.user = user_instance
        return professional_instance


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ("id", "unique_id", "name", "description")

    def get_extra_kwargs(self):
        extra_kwargs = super().get_extra_kwargs()
        request: Request | None = self.context.get("request", None)
        if request is not None and request.method == "POST":
            extra_kwargs["profession"] = {"required": True}
        return extra_kwargs
