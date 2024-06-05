from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USER_TYPES = [
        ('employee', 'Employee'),
        ('employer', 'Employer'),
    ]
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    phone_code = models.CharField(max_length=5, default='+254')
    phone_number = models.CharField(
        max_length=13, unique=True, blank=True, null=True)
    profile_picture = models.FileField(blank=True, null=True)
    user_type = models.CharField(
        max_length=20, choices=USER_TYPES, default="employee")

    def __str__(self):
        return self.username


class StudentMarks(models.Model):
    database1 = models.FloatField(null=False)
    database2 = models.FloatField(null=False)

    def __str__(self):
        return self.database1


class BookingAppointment(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
