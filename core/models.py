from django.db import models

# Create your models here.
class CustomUser(models.Model):
    USER_TYPES = [
        ('employee', 'Employee'),
        ('employer', 'Employer'),
    ]

    first_name = models.CharField(max_length=50, blank= True, null =True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_code = models.CharField(max_length= 5, default= '+254')
    phone_number = models.CharField(max_length=13, unique=True, blank=True, null=True)
    password = models.CharField(max_length=255)
    profile_picture = models.FileField()
    user_type = models.CharField(max_length =20, choices=USER_TYPES,default="employee")

    def __str__(self):
        return  f"{self.first_name} {self.last_name}"
