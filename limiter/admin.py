from django.contrib import admin
from .models import *


class UsersAdmin(admin.ModelAdmin):
    """
    Admin class for manage users
    """
    list_display = ('pk', 'user_name', 'weight')


class UserProcessQueueAdmin(admin.ModelAdmin):
    """
    Admin class for manage process
    """
    list_display = ('user', 'time_to_complete', 'time_completed', 'is_stopped', 'is_finished')


admin.site.register(Users, UsersAdmin)
admin.site.register(UserProcessQueue, UserProcessQueueAdmin)
