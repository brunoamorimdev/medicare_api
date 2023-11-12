from django.db import models
from core.models import BaseModel
from user.models import BaseUserProfile
from professional.managers import ProfessionalManager


class Profession(BaseModel):
    name = models.CharField(max_length=80, blank=True, null=False, default="")
    description = models.TextField(max_length=128, blank=True, null=True, default="")

    class Meta:
        db_table = "profession"
        verbose_name = "profession"
        verbose_name_plural = "professions"


class Professional(BaseUserProfile):
    profession = models.ManyToManyField(Profession, related_name="profession")

    objects = ProfessionalManager()

    class Meta:
        db_table = "professional"
        verbose_name = "professional"
        verbose_name_plural = "professionals"
