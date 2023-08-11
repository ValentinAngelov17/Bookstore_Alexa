from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission

from bookstore_django_project.auth_web.models import AppUser, StaffGroup


class CustomUserAdmin(UserAdmin):
    model = AppUser
    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    ordering = ['email']
    list_filter = ['is_staff', 'is_superuser', 'groups']


# Register the custom admin class
admin.site.register(AppUser, CustomUserAdmin)


class StaffGroupAdmin(admin.ModelAdmin):
    filter_horizontal = ('permissions',)


admin.site.register(StaffGroup, StaffGroupAdmin)
