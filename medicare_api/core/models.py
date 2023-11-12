from django.db import models
import uuid


class BaseModel(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        abstract = True
        ordering = ["-created_at"]
