from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class SignupView(TemplateView):
    template_name = 'workers/index.html'

class Workers(TemplateView):
    template_name = 'workers/index.html'

class Owners(TemplateView):
    template_name = 'owners/index.html'

class Contractors(TemplateView):
    template_name = 'contractors/index.html'
