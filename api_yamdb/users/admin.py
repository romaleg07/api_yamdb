from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = (
        'pk',
        'username',
        'email',
        'first_name',
        'last_name',
        'bio',
        'role',
    )
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'BIO',
            {
                'fields': (
                    'bio',
                    'role',
                ),
            },
        ),
    )
    empty_value_display = '-пусто-'


admin.site.register(User, CustomUserAdmin)
