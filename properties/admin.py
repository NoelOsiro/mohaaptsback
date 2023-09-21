# In your app's admin.py file

from django.contrib import admin
from .models import Property

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'property_type', 'price', 'square_feet', 'no_bedrooms')
    list_filter = ('property_type',)
    search_fields = ('name', 'address')
