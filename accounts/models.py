from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=30)
    contact_mail = models.EmailField()
    contact_number = models.IntegerField(null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
        

class Employee(models.Model):
    name = models.CharField(max_length=30, null=True)
    surname = models.CharField(max_length=30, null=True)
    added_date = models.DateTimeField('date when added', auto_now_add=True)
    employer = models.ForeignKey(Company, on_delete=models.CASCADE, null=False)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    def has_access(self,obj):
        try:
            obj.authorize(self)
        except:
            print("uhh wtf nie mam authorize()!")

    def __str__(self):
        return f"{self.name} {self.surname}"
    
