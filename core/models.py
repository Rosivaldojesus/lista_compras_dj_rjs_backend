from calendar import c
from email.policy import default
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class List(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name
