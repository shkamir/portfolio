from __future__ import unicode_literals
from django.contrib import admin

# Register your models here.
# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Project


class ProjectManager(admin.ModelAdmin):
    list_display = ('title', 'tools',)
    list_filter = ('pub_date',)
    search_fields = ('title', 'description', 'tools', 'url',)


admin.site.register(Project, ProjectManager)
