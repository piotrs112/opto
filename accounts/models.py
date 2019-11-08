from django.db import models
from django.contrib.auth.models import AbstractUser, User


class Company(models.Model):
    name = models.CharField(max_length=30)
    contact_mail = models.EmailField()
    contact_number = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class Employee(models.Model):
    name = models.CharField(max_length=30, null=True)
    surname = models.CharField(max_length=30, null=True)
    added_date = models.DateTimeField('date when added', auto_now_add=True)
    employeeOf = models.ForeignKey(Company, on_delete=models.CASCADE, null=False)