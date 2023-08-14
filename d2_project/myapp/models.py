from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=50)
    uname=models.CharField(max_length=50)
    email=models.EmailField()
    mobile=models.IntegerField()
    password=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    

    def  __str__(self):
        return self.name
    
