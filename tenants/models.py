from django.db import models
from properties.models import Property
from staff.models import Staff

class Tenant(models.Model):
    # Tenant information
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    image = models.ImageField(upload_to='tenant_images/', null=True, blank=True)
    identification_pdf = models.FileField(upload_to='tenant_identification/', null=True, blank=True)
    lease_agreement_pdf = models.FileField(upload_to='tenant_lease_agreements/', null=True, blank=True)

    # Property booking
    booked_property = models.ForeignKey( Property, on_delete=models.SET_NULL, null=True, blank=True)
    booking_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.full_name

from django.db import models

class ServiceRequest(models.Model):
    # Request details
    tenant = models.ForeignKey('Tenant', on_delete=models.CASCADE)
    request_date = models.DateField()
    description = models.TextField()
    
    # Status
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('unsolved', 'Unsolved'),
        ('resolved', 'Resolved'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    # Additional fields as needed
    assigned_staff = models.ForeignKey( Staff, on_delete=models.SET_NULL, null=True, blank=True)
    completion_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Request by {self.tenant.full_name} - {self.request_date}"
