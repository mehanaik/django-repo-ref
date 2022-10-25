# COMP 8347 Lab 3
# GROUP 2

from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=200)

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=100)
    available = models.BooleanField(default=True)

class Client(User):
    PROVINCE_CHOICES = [
        ('AB', 'Alberta'),
        ('MB', 'Manitoba'),
        ('ON', 'Ontario'),
        ('QC', 'Quebec'),]

    company = models.CharField(max_length=50)
    shipping_address = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=20)
    province=models.CharField(max_length=2, choices=PROVINCE_CHOICES, default='ON')
    interested_in = models.ManyToManyField(Category)
