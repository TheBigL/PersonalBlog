from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Portfolio
from django.shortcuts import render, redirect

# Create your views here.
class PortfolioListView(ListView):
    model = Portfolio
    template_name = 'portfolio.html'
    context_object_name = 'portfolios'

