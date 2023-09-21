# In your app's admin.py file

from django.contrib import admin
from .models import Tenant, ServiceRequest

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'booking_date')
    search_fields = ('full_name', 'email', 'phone_number')
    list_filter = ('booking_date',)

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'request_date', 'status', 'assigned_staff', 'completion_date')
    list_filter = ('status', 'assigned_staff')
    search_fields = ('tenant__full_name', 'description')

