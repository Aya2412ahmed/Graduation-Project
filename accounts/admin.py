from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "age",
        'is_admmin',
        'is_student',
        'is_staaff', 'is_staff', 'phone',  'name_ar',
        'slug',
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ('age', 'is_student', 'is_admmin', 'nid', 'is_staaff', 'phone',
                                        'name_ar', 'slug',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ('age', 'is_student', 'is_admmin', 'nid', 'is_staaff', 'phone',
                                                                  'name_ar', 'slug',)}),)


admin.site.register(CustomUser, CustomUserAdmin)
