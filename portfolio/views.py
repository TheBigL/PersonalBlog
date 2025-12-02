from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Portfolio
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator

# Create your views here.
