from django.urls import path
from . import views

urlpatterns =[
		path("", views.home, name ="home"),
		path("corona/", views.corona, name ="corona"),
		path("services/", views.services, name ="services"),
		path("contact/", views.contact, name ="contact"),
		path("clients/", views.displayClients, name ="displayClients"),
		path("employees/", views.displayEmployees, name ="display"),
		path("login/",views.login, name="login"),

]