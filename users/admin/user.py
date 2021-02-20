from django.contrib import admin

from users.models.user import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
