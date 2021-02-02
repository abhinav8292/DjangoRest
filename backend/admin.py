from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import*

# Register your models here.


class UserAdmin(UserAdmin):
    model = User


admin.site.register(User, UserAdmin)
admin.site.register(Posts)
