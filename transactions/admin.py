# In your app's admin.py file

from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('date', 'description', 'amount', 'transaction_type', 'property', 'tenant')
    list_filter = ('transaction_type',)
    search_fields = ('description', 'property__name', 'tenant__full_name')
