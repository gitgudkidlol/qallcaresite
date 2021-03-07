from django.db import models


class Clinic(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Patient(models.Model):
	fromClinic = models.ForeignKey(Clinic,on_delete=models.CASCADE)
	firstname = models.CharField(max_length=200)
	lastname= models.CharField(max_length=200)
	diagnosis=models.BooleanField()
	id=models.int()

	def __str__(self):
		return (self.firstname + self.lastname)


# Create your models here.
