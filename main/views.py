from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Clinic,Patient
from .forms import UploadNewClinic, UploadNewPatient
import time

def home(response):
	return render(response, "main/home.html",{"name":'test'})

def displayClinics(response):
	cnt=1
	ls = Clinic.objects.all()
	for each in ls:
		Clinic.objects.get(id=cnt)
		cnt=cnt+1

	if response.method =="POST":
		form = UploadNewClinic(response.POST)
		if form.is_valid():
			n= form.cleaned_data["name"]
			t = Clinic(name=n)
			t.save()
	else:
		form=UploadNewClinic
	return render(response, "main/displayClinics.html",{'ls':ls,'form':form})

def display(response, id):
	ls = Clinic.objects.get(id=id)
	form=UploadNewPatient()
	return render(response, "main/display.html",{'ls':ls,'form':form})

# def upload(response):
# 	if response.method =="POST":
# 		form = UploadNewClinic(response.POST)
# 		if form.is_valid():
# 			n= form.cleaned_data["name"]
# 			t = Clinic(name=n)
# 			t.save()
# 			print(t.id)
# 		return HttpResponseRedirect("/%i" %t.id)
# 	else:
# 		form=UploadNewClinic
# 	return render(response, "main/upload.html", {"form":form})

def login(response):
	return render(response, "main/login.html",{})


#Statics
def corona(response):
	return render(response, "main/corona.html")

def services(response):
	return render(response, "main/services.html")

def contact(response):
	return render(response, "main/contact.html")


