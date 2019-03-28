from django.forms import ModelForm
from .models import student

class regForm(ModelForm):
	class Meta:
		model=student
		fields=["name","password"]

class logForm(ModelForm):
	class Meta:
		model=student
		fields=["name","password"]