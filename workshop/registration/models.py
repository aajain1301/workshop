from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    contact = models.PositiveIntegerField(default=1)
    college_name = models.CharField(max_length=50)
    branch_name = models.CharField(max_length=50)
    sem = models.IntegerField(default=1)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.first_name
