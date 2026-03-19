from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_approved')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone', 'gotra', 'village', 'profile_pic', 'is_approved')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone', 'gotra', 'village', 'profile_pic', 'is_approved')}),
    )
