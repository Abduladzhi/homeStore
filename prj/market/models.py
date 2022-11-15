from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Provider(User):
    name = models.CharField(max_length=255, default='')
    phone = models.CharField(max_length=255, default='')
    rating = models.IntegerField(default=0)

class Consumer(User):
    name = models.CharField(max_length=255, default='')
    phone = models.CharField(max_length=255, default='')
    address = models.TextField(default='')
    geo_location = models.CharField(max_length=255, default='')
    
class Category(models.Model):
    name = models.CharField(max_length=255, default='')

class Product(models.Model):
    name = models.CharField(max_length=255, default='')
    image = models.ImageField(upload_to='product')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)