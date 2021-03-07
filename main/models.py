from django.db import models
import os
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

class Client(models.Model):
	fromUser = models.ForeignKey(User,on_delete=models.CASCADE)
	name = models.CharField(max_length=200)


	def __str__(self):
		return self.name

class Patient(models.Model):
	fromClient = models.ForeignKey(Client,on_delete=models.CASCADE)
	firstname = models.CharField(max_length=200)
	lastname= models.CharField(max_length=200)
	notes = models.CharField(default= "NA", max_length=200)	
	# report=models.FileField()
	date=models.DateField(auto_now=False)

	def __str__(self):
		return (self.firstname +" "+ self.lastname)


class pdfFile(models.Model):
	fromPatient = models.ForeignKey(Patient,on_delete=models.CASCADE)
	name=models.CharField(max_length=200)
	pdf=models.FileField(validators=[FileExtensionValidator(["pdf"])])
	date=models.DateField(auto_now=False)

	def __str__(self):
		return(self.name)
# Create your models here.
