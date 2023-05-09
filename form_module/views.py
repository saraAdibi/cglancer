# views.py
from django.views.generic.edit import CreateView
from django.shortcuts import render
from .forms import ContactForm


class ContactUsView(CreateView):
    form_class = ContactForm
    template_name = 'form1.html'
    success_url = '/'