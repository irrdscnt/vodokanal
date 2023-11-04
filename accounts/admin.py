from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
    "username",
    "email",
    "phone",
    "is_admin",
    "is_staff",
    "debt"
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("phone","is_admin","debt")}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("phone","is_admin","debt")}),)
admin.site.register(CustomUser, CustomUserAdmin)
