from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=80)
    website = models.CharField(max_length=100)
    iconUrl = models.CharField(max_length=120)
