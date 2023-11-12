from functools import cached_property
from django.db import models
from django.contrib.auth.models import AbstractUser
from user.managers import UserManager
from core.models import BaseModel


class User(BaseModel, AbstractUser):
    email = models.EmailField(blank=False, unique=True, default="")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("username", "password", "first_name", "last_name")

    objects = UserManager()

    class Meta:
        db_table = "auth_user"
        verbose_name = "auth_user"
        verbose_name_plural = "auth_users"


class BaseUserProfile(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile")

    @cached_property
    def full_name(self):
        return f"{self.user.get_full_name()}"

    @cached_property
    def email(self):
        return f"{self.user.email}"

    class Meta:
        abstract = True
