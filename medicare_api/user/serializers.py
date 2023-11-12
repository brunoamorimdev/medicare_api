import rest_framework.serializers as serializers
from user.models import User
from rest_framework.request import Request


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "unique_id",
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
        )

    def get_extra_kwargs(self):
        extra_kwargs = super().get_extra_kwargs()
        request: Request | None = self.context.get("request", None)

        extra_kwargs["unique_id"] = {"read_only": True}
        extra_kwargs["password"] = {"write_only": True}
        # Set 'required' to True for fields in create operation
        extra_kwargs["first_name"] = {"required": False}
        extra_kwargs["last_name"] = {"required": False}
        extra_kwargs["username"] = {"required": False}
        extra_kwargs["email"] = {"required": False}
        extra_kwargs["password"] = {"required": False, **extra_kwargs["password"]}

        if request is not None and request.method == "POST":
            # Set 'required' to True for fields in create operation
            extra_kwargs["first_name"] = {"required": True}
            extra_kwargs["last_name"] = {"required": True}
            extra_kwargs["username"] = {"required": True}
            extra_kwargs["email"] = {"required": True}
            extra_kwargs["password"] = {**extra_kwargs["password"], "required": True}

        return extra_kwargs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
