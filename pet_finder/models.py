from django.db import models

STATE_CHOICES = []

class Pet(models.Model):
    img = 
    name = models.CharField(max_length=60)
    animal = models.Charfield(max_length=15)
    gender = models.CharField(max_length=7)
    breed = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=60, blank=True, null=True)
    age = models.CharField(max_length=10, blank=True, null=True)
    lost = models.DateField
    address = models.CharField(max_length=75, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=2)
    reward = models.CharField(max_length=15, blank=True, null=True)
    description = models.TextField(max_length=400, blank=True, null=True)

