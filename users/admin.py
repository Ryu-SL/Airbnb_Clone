from django.contrib import admin
from django.db.models.base import Model
from . import models
from django.contrib.auth.admin import UserAdmin


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """Custom User Admin"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "language",
                    "currency",
                    "birthdate",
                    "bio",
                    "superhost",
                )
            },
        ),
    )
