from django.db import models
from users.models import User
from PIL import Image


STATE_CHOICES = []

class Pet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='pet/', blank=True, null=True)
    name = models.CharField(max_length=60)
    animal = models.CharField(max_length=15)
    gender = models.CharField(max_length=7)
    breed = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=60, blank=True, null=True)
    age = models.CharField(max_length=10, blank=True, null=True)
    lost = models.DateField(auto_now_add=False)
    last_seen = models.CharField(max_length=75, blank=True, null=True)
    address = models.CharField(max_length=75, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    reward = models.CharField(max_length=3, blank=True, null=True)
    amount = models.PositiveIntegerField(blank=True, null=True)
    description = models.TextField(max_length=400, blank=True, null=True)

    def __str__(self):
        return f'Pet: {self.user}, {self.name}, {self.animal}, {self.gender}, {self.breed}, {self.color}, {self.age}, {self.lost}, {self.last_seen}, {self.address}, {self.city}, {self.state}, {self.reward}, {self.description}'

class FoundPet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='found/', blank=True, null=True)
    name = models.CharField(max_length=60, blank=True, null=True)
    animal = models.CharField(max_length=15)
    gender = models.CharField(max_length=7)
    breed = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=60, blank=True, null=True)
    found = models.TextField(max_length=300)
    description = models.TextField(max_length=400, blank=True, null=True)



class Post(models.Model):
    pass
