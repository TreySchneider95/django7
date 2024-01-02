from django.db import models

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length = 200)
    height = models.FloatField()
    weight = models.FloatField()
    dietary_preference = models.CharField(max_length = 200)