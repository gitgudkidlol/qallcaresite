from django.contrib import admin
from .models import Client, Patient, pdfFile

admin.site.register(Client)
admin.site.register(pdfFile)
admin.site.register(Patient)
# Register your models here.
