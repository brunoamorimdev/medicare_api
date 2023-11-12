from django.db import models
from core.models import BaseModel
from user.models import BaseUserProfile


class ProfessionalSpecialization(BaseModel):
    name = models.CharField(max_length=80, blank=True, null=False, default="")
    description = models.TextField(max_length=128, blank=True, null=True, default="")

    class Meta:
        db_table = "professional_specialization"
        verbose_name = "professional specialization"
        verbose_name_plural = "professional specializations"


class Professional(BaseUserProfile):
    specializations = models.ManyToManyField(
        ProfessionalSpecialization, related_name="professionals"
    )

    class Meta:
        db_table = "professional"
        verbose_name = "professional"
        verbose_name_plural = "professionals"
