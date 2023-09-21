from django.db import models

class Property(models.Model):
    PROPERTY_TYPES = (
        ('commercial', 'Commercial'),
        ('residential', 'Residential'),
    )

    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    name = models.CharField(max_length=100)
    address = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    square_feet = models.PositiveIntegerField()
    no_bedrooms = models.PositiveSmallIntegerField(null=True, blank=True)
    
    # Additional fields specific to commercial properties
    no_offices = models.PositiveSmallIntegerField(null=True, blank=True)
    
    # Add more fields as needed
    # For example, you can add fields for amenities, parking, etc.

    def __str__(self):
        return self.name
