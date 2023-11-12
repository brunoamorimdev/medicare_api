from typing import Any
import django.db.models as models
from user.models import User


class ProfessionalManager(models.Manager):
    def create_professional(self, **kwargs: Any) -> Any:
        user_data = kwargs.pop("user_data", None)
        user_instance = User.objects.create_user(data=user_data)
        professional_instance = self.create(user=user_instance, **kwargs)
        return professional_instance
