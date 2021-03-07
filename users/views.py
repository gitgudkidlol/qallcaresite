from django.shortcuts import render, redirect
from .forms import RegisterForm
# from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def register(response):
	if response.method =="POST":
		form = RegisterForm(response.POST)
		if form.is_valid():
			print("is valid")
			form.save()
			return redirect("/")
		else:
			pass
	else:
		form = RegisterForm()
	return render(response,"users/register.html",{"form":form})
