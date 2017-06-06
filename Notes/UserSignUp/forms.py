from django import forms
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from .models import NotesDatabase

class SignUpForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput())
	username = forms.CharField(max_length = 20)
	first_name = forms.CharField(max_length= 20)
	class Meta:
		model = User
		fields = ['username', 'password', 'first_name']
	
class LogForm(forms.Form):
	password = forms.CharField(widget = forms.PasswordInput())
	username = forms.CharField(max_length = 20)
	class Meta:
		model = User
		fields = ['username', 'password']	

class MyNotes(forms.Form):
	noteText = forms.CharField(max_length=1000)
	tags = forms.CharField(max_length=200)
	sharedwith = forms.CharField(max_length=200)
	class Meta:
		model = NotesDatabase
		fields = ['noteText', 'tags']

class TagSearch(forms.Form):
	search = forms.CharField(max_length=20)
	class Meta:
		model = NotesDatabase
		fields = ['search']
   
    			