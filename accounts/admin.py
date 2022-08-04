from django.contrib import admin
from .models import User, UserProfile
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomerUser(UserAdmin):
    list_display = ('email','first_name', 'username', 'role', 'is_active')
    ordering = ('-date_joined',)
    filter_horizontal=()
    list_filter =()
    fieldsets =()

admin.site.register(User, CustomerUser)
admin.site.register(UserProfile)