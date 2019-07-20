from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=50)
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    contact = models.PositiveIntegerField(default=1,unique=True)
    txn_id  = models.CharField(max_length=40)
    email   = models.EmailField(unique=True)
    college = models.CharField(max_length=50)
    branch  = models.CharField(max_length=50)
    course  = models.CharField(max_length=50)
    sem     = models.IntegerField(default=1)
    address = models.TextField(blank=True)
    pay_mode= models.CharField(max_length=50)


    def __str__(self):
        return self.first_name
