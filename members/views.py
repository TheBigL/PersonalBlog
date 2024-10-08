
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from django.contrib.auth.forms import *
from django.urls import reverse_lazy
from .forms import MemberCreationForm

from .models import Member


# Create your views here.
class SignUpView(CreateView):
    form = MemberCreationForm
    success_url = reverse_lazy('/')
    template = 'registeruser.html'
    success_message = "You have successfully registered!"
    