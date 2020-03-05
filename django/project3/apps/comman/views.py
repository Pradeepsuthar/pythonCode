from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views.generic import TemplateView, CreateView
# Create your views here.

class HomeView(TemplateView):
    template_name = 'comman/index.html'

class Login(TemplateView):
    template_name = 'comman/login.html'
