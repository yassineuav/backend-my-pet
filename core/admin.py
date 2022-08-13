from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core.models import User, Post, Like


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass


admin.site.register(Post)
admin.site.register(Like)
