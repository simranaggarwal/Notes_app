from __future__ import unicode_literals
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render,redirect, reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as log_out
from django.template import loader
from django.views.generic import View
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import SignUpForm, LogForm, MyNotes, TagSearch
from .models import NotesDatabase, Tags, Sharednames

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

 				return redirect(reverse('UserSignUp:mynotes'))
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
 				return redirect(reverse('UserSignUp:login'))
 		return render(request, self.template_name, {'form': form})

class NotesCreate(View):
	form_class = MyNotes
	template_name = 'UserSignUp/mynotes.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form,
													'username': request.user.username})

	def post(self, request):
		form = self.form_class(request.POST, None)
		
		if request.user.is_authenticated:
			if form.is_valid():
				noteText = form.cleaned_data['noteText']
				tags = form.cleaned_data['tags']
				username = request.session.get('username', False)
				sharedwith = form.cleaned_data['sharedwith']
				sharedunames = sharedwith.split(",")
				mytags = tags.split(",")
				#print mytags

				UserInstance=User.objects.get(username=username)
				NotesDatabaseInstance = NotesDatabase.objects.create(username = UserInstance, noteText = noteText)
				for tag in mytags:
					created,t1 = Tags.objects.get_or_create(myTag = tag)
					created.myNote.add(NotesDatabaseInstance)
				for name in sharedunames:
					try:
						userExist=User.objects.get(username=name)
						created,u1 = Sharednames.objects.get_or_create(shareduser = name)
						created.mysharedname.add(NotesDatabaseInstance)
					except Exception as e:
						print "this user "+ name + "does not exist "
				return redirect(reverse('UserSignUp:mynotes'))
		else:
			return redirect(reverse('UserSignUp:login'))
		return render(request, self.template_name, {'form': form,
													'username': request.user.username})


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
				print "username --> "+ username
				UserInstance = User.objects.get(username=username)
				myVar = Tags.objects.filter(myTag = tag)
				NotesDatabaseInstance = NotesDatabase.objects.filter(tags = myVar, username = UserInstance)
				
				try:
					SharedInstance=Sharednames.objects.get(shareduser=username)
					NotesDatabaseInstance2=NotesDatabase.objects.filter(sharednames=SharedInstance,tags=myVar)
					print NotesDatabaseInstance2
					return render(request, 'UserSignUp/search.html', {'myVar':NotesDatabaseInstance,'shared':NotesDatabaseInstance2})
				except:
					print "in except ---->>>>>"
				return render(request, 'UserSignUp/search.html', {'myVar':NotesDatabaseInstance})
		else:
			return redirect(reverse('UserSignUp:login'))
		return render(request, self.template_name, {'form': form})


def logout(request):
	log_out(request)
	return redirect(reverse('UserSignUp:login'))














