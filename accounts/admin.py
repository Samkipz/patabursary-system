from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import MyUserCreationForm, MyUserChangeForm
from .models import User, Applicant, Staff


class UserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = User
    list_display = ('email', 'first_name', 'last_name', 'gender', 'is_applicant', 'is_staff', 'is_active', 'phone_no')
    list_filter = ('gender', 'is_staff', 'is_applicant', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'gender', 'phone_no')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_applicant')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')
            }
        ),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(User, UserAdmin)
admin.site.register(Applicant)
admin.site.register(Staff)
