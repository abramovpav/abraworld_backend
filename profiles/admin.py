from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from profiles.models import Profile

admin.autodiscover()

# Register your models here.


class ProfileInline(admin.StackedInline):
    model = Profile


class ExtendedUserAdmin(UserAdmin):
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User, ExtendedUserAdmin)
