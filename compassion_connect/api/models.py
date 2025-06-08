# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [("Regional_Director","Regional Director"),
        ("Country_Director","Country Director"),
        ("Project_director","Project Director"),
                    ("PF","PF"),("CDO_SDR","CDO SDR"),
                    ("CDO_HEALTH","CDO Health")]
    GENDER_CHOICES=[("Female","Female"),("Male","Male")]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    name= models.CharField(max_length=100)
    gender=models.CharField(max_length=10,choices=GENDER_CHOICES)
    region=models.CharField(max_length=30,null=True,blank=True)
    country=models.CharField(max_length=50,null=True,blank=True)
    project_code=models.CharField(max_length=20,null=True,blank=True)
    cluster=models.CharField(max_length=100,null=True,blank=True)


