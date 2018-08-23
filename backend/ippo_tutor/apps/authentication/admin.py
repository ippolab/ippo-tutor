from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .models import User


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    model = User
    list_display = ['username', 'is_staff']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (
            'Permissions', {'fields': (
                'is_active',
                'is_tutor',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'is_tutor', 'password1', 'password2'),
        }),
    )
