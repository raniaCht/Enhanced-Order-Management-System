from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Order(models.Model):

    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("processing", "Processing"),
        ("shipped", "Shipped"),
        ("delivered", "Delivered"),
    )


    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default="pending")
    price= models.PositiveIntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title + " - " + str(self.id)
    

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
