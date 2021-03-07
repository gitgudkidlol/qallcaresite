from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Client, User#, Patient
from .forms import UploadNewEmployee
import time

def home(response):
	
	return render(response, "main/home.html",{"name":'test'})

def displayClients(response):

	if response.user.is_staff==False:
		return(response,"/")
	ls = Client.objects.all()
	return render(response, "main/displayClients.html",{'ls':ls})

def displayEmployees(response):
	ls= response.user.client_set.get()
	return render(response, "main/display.html",{'ls':ls})

def login(response):
	return render(response, "main/login.html",{})


#Statics
def corona(response):
	return render(response, "main/corona.html")

def services(response):
	return render(response, "main/services.html")

def contact(response):

	return render(response, "main/contact.html")


