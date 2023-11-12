import sys
import os
import django

sys.dont_write_bytecode = True
os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"medicare_api.settings")
django.setup()

from user.models import User
from django.contrib.auth.models import Permission, Group


def main():
    # user = User(email="bruno@leaderweb.comb")
    # user.user_permissions.add()
    pass
