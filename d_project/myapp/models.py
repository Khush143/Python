from django.db import models

# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=100, unique=True)
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.PositiveIntegerField()
	password=models.CharField(max_length=100)
	profile_pic=models.ImageField(default="",upload_to="profile_pic/")

	def __str__(self):
		return self.fname+" "+self.lname


