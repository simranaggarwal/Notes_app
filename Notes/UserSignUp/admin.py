# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import NotesDatabase, Tags, Sharednames

admin.site.register(NotesDatabase)
admin.site.register(Tags)
admin.site.register(Sharednames)
