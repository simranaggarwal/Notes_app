from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField

from django.contrib.auth.models import User

class NotesDatabase(models.Model):
    username = models.ForeignKey(User)
    noteText = models.CharField(max_length=1000)

    def __str__(self):
		return self.noteText
		
class Tags(models.Model):
	myTag = models.CharField(max_length=15)
	myNote = models.ManyToManyField(NotesDatabase)

class Sharednames(models.Model):
	shareduser = models.CharField(max_length=50)
	mysharedname = models.ManyToManyField(NotesDatabase)