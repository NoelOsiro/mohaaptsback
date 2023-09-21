from django.db import models

class DutyDay(models.Model):
    DAY_CHOICES = (
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    )

    staff_p = models.ForeignKey('Staff', on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=20, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.staff.full_name}'s Duty on {self.get_day_of_week_display()}"

    class Meta:
        unique_together = ('staff_p', 'day_of_week')


class Staff(models.Model):
    # Staff information
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    image = models.ImageField(upload_to='staff_images/', null=True, blank=True)
    role = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField()
    
    # Additional fields as needed
    address = models.TextField()
    duty_schedule = models.ManyToManyField('DutyDay', blank=True)

    def __str__(self):
        return self.full_name
