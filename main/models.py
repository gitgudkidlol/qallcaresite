from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
	fromUser = models.ForeignKey(User,on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	

	def __str__(self):
		return self.name

class Patient(models.Model):
	fromClient = models.ForeignKey(Client,on_delete=models.CASCADE)
	firstname = models.CharField(max_length=200)
	lastname= models.CharField(max_length=200)
	diagnosis = models.CharField(default= "NA", max_length=200)	
	date=models.DateField(auto_now=False)

	def __str__(self):
		return (self.firstname +" "+ self.lastname)


# Create your models here.
