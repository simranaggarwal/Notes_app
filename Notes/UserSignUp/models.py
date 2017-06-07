# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
# Create your models here.

from django.contrib.auth.models import User

class NotesDatabase(models.Model):
    username = models.ForeignKey(User)
    noteText = models.CharField(max_length=1000)
    sharedWith=models.ManyToManyField(User)

    def __str__(self):
    	return self.noteText+"	user --->. "+self.username.username

class Tags(models.Model):
 	myTag=models.CharField(max_length=100)
 	myNote=models.ManyToManyField(NotesDatabase)

 	def __str__(self):
 		return self.myTag
