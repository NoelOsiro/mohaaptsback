# In your app's admin.py file

from django.contrib import admin
from .models import Staff

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'role', 'salary')
    list_filter = ('role','duty_schedule')
    search_fields = ('duty_schedule', 'full_name')


