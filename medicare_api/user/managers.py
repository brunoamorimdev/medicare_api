from typing import Any
import django.db.models as models
from django.core.exceptions import ValidationError


class UserManager(models.Manager):
    def create_user(self, **kwargs: dict[Any]):
        if kwargs is not None:
            user = self.model(**kwargs)
            user.set_password(raw_password=kwargs["password"])
            user.save()
            return user
        else:
            raise ValidationError("No User data")
