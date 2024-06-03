from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Pizza(models.Model):
  name = models.CharField(max_length=100)
  ingredients = models.CharField(max_length=500)
  description = models.TextField(max_length=250)
  location = models.CharField(max_length=50)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse("pizza-detail", kwargs={"pk": self.id})
  