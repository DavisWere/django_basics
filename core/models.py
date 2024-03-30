from django.db import models
from django.contrib.auth.models import AbstractUser

    
class CustomUser(AbstractUser):
    USER_TYPES = [
        ('employee', 'Employee'),
        ('employer', 'Employer'),
    ]
    first_name = models.CharField(max_length=50, blank= True, null =True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    phone_code = models.CharField(max_length= 5, default= '+254')
    phone_number = models.CharField(max_length=13, unique=True, blank=True, null=True)
    profile_picture = models.FileField(blank=True, null=True)
    user_type = models.CharField(max_length =20, choices=USER_TYPES,default="employee")

    def __str__(self):
        return self.username
    

