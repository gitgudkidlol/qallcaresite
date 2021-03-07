from django.urls import path
from . import views

urlpatterns =[
		path("", views.home, name ="home"),
		path("corona/", views.corona, name ="corona"),
		path("services/", views.services, name ="services"),
		path("contact/", views.contact, name ="contact"),
		path("clinics/", views.displayClinics, name ="displayClinics"),
		path("clinics/<int:id>",views.display, name="display"),
		# path("upload/",views.upload, name="upload"),
		path("login/",views.login, name="login"),

]