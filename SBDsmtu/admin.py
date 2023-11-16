from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from .models import Role, UserProfile

admin.site.register(Role)

admin.site.register(UserProfile)

