from django.db import models
from properties.models import Property
from tenants.models import Tenant

class Transaction(models.Model):
    # Transaction details
    date = models.DateField()
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    property = models.ForeignKey( Property, on_delete=models.SET_NULL, null=True, blank=True)
    tenant = models.ForeignKey( Tenant, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Transaction type
    TRANSACTION_TYPES = (
        ('income', 'Income'),
        ('expense', 'Expense'),
    )
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)

    def __str__(self):
        return f"{self.date} - {self.description}"
