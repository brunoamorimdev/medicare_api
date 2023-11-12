from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


class UserPermissionsSelectors:
    content_type_model = ContentType

    @classmethod
    def content_type_list(self, filters={}):
        return self.content_type_model.objects.filter(**filters)
