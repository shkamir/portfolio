# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.contrib.messages.views import SuccessMessageMixin

from django.core.mail import send_mail, get_connection
from django.conf import settings

from .forms import ContactForm
from .models import Project

class ProjectListAndFormView(SuccessMessageMixin, ListView, FormView):
    model = Project 
    template_name = 'mainpage/main.html'
    context_object_name = 'list_projects' 
    queryset = Project.objects.all().order_by("-pub_date")
    object_list = None

    form_class = ContactForm
    success_url = '/' 
    success_message = 'Your Form has been successfully submitted!'

    def form_valid(self, form):
        my_form = form.cleaned_data
        myCon = get_connection('django.core.mail.backends.console.EmailBackend')
        send_mail(
            my_form['name'],
            my_form['message'],
            my_form.get('email', 'noreply@example.com'),
            ['shekooha696@gmail.com'],
            fail_silently=False
        )
        return super(ProjectListAndFormView, self).form_valid(form)
