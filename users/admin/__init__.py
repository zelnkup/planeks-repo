from django.contrib.auth.models import Group

from users.admin.user import UserAdmin  # noqa
from django.contrib import admin

admin.site.unregister(Group)
