from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import userAccount
from django.contrib.auth.models import User

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class userAccountInline(admin.StackedInline):
    model = userAccount
    can_delete = False
    verbose_name_plural = 'userAccount'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (userAccountInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)