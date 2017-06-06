# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.template import loader
from django.views.generic import View
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User
#from .models import user_info
from .forms import SignUpForm, LogForm, MyNotes, TagSearch
from .models import NotesDatabase

def signUp(request):
    return render(request, 'UserSignUp/SignUpPage.html', {})

class LoginForm(View):	
	form_class = LogForm
	template_name = 'UserSignUp/SignUpPage.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST, None)
		
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
 			
 			user = authenticate(username=username, password=password)
 			if user is not None:
 				login(request, user)
 				request.session['username'] = username
				messages.add_message(request, messages.INFO, username)

 				return redirect("http://127.0.0.1:8000/myapp/mynotes")
 		return render(request, self.template_name, {'form': form})


class  UserFormView(View):
	form_class = SignUpForm
	template_name = 'UserSignUp/registration_form.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST, None)
		
		if form.is_valid():
			user = form.save(commit=False)

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			first_name = form.cleaned_data['first_name']


			user.username = username
			user.first_name = first_name
			user.set_password(password)
			user.save()
 			
 			user = authenticate(username=username, password=password)
 			if user is not None:
 				return redirect("http://127.0.0.1:8000/myapp/login/")
 		return render(request, self.template_name, {'form': form})

class NotesCreate(View):
	form_class = MyNotes
	template_name = 'UserSignUp/mynotes.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST, None)
		
		if request.user.is_authenticated:
			if form.is_valid():
				noteText = form.cleaned_data['noteText']
				tags = form.cleaned_data['tags']
				#username = form.cleaned_data['username']
				username = request.session.get('username', False)
				sharedwith = form.cleaned_data['sharedwith']
				sharedunames = sharedwith.split(",")
				mytags= tags.split(",")
				print mytags
				UserInstance=User.objects.get(username=username)
				NotesDatabaseInstance = NotesDatabase.objects.create(username = UserInstance, noteText = noteText, tags = mytags, sharedwith= sharedunames)
				return redirect("http://127.0.0.1:8000/myapp/search/")	
		else:
			return redirect("http://127.0.0.1:8000/myapp/login/")
		return render(request, self.template_name, {'form': form})


class SearchTag(View):
	form_class = TagSearch
	template_name = 'UserSignUp/search.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST, None)
		
		if request.user.is_authenticated:
			if form.is_valid():
				tag = form.cleaned_data['search']
				username = request.session.get('username', False)
				#print username
				UserInstance=User.objects.get(username=username)
				myVar = NotesDatabase.objects.filter(username = UserInstance).filter(tags__contains=[tag])
				myAnother = NotesDatabase.objects.filter(sharedwith__contains= [username]).filter(tags__contains=[tag])
				print myAnother
				return render(request, 'UserSignUp/search.html', {'myVar':myVar, 'myAnother':myAnother})
		else:
			return redirect("http://127.0.0.1:8000/myapp/login/")
		return render(request, self.template_name, {'form': form})


def loggout(request):
	#del request.session['username']
	logout(request)
	return redirect("http://127.0.0.1:8000/myapp/login/")














