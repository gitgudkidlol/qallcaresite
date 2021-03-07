from django import forms

class UploadNewClinic(forms.Form):
	name=forms.CharField(label="Clinic Name",max_length=200)

class UploadNewPatient(forms.Form):
	firstname=forms.CharField(label="First name",max_length=200)
	lastname= forms.CharField(label="Last name",max_length=200)
	diagnosis=forms.BooleanField(label="Positive")

# class UploadNewPatient(forms.Form):