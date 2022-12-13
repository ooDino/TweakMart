from django.contrib import admin
from django.contrib.admin import StackedInline
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .forms import EditProfileForm

class AccountInline(StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profies'

class CustomUserAdmin(UserAdmin):
    inlines = (AccountInline, )

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

