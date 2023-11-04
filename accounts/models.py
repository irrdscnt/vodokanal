from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    phone = models.CharField(blank=True, null=True, max_length=100)
    email=models.EmailField(null=True)
    debt=models.IntegerField(blank=True,null=True)
