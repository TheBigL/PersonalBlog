from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Portfolio
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator

# Create your views here.
class PortfolioListView(ListView):
    model = Portfolio
    template_name = 'portfolio.html'
    context_object_name = 'portfolios'

class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfoliodetail.html'

@method_decorator(login_required, name='dispatch')
class AddPortfolioView(CreateView):
    model = Portfolio
    fields = ['name', 'description', 'img', 'link']
    template_name = 'portfolio/addportfolio.html'
    success_url = '/portfolio/'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def handle_no_permission(self):
        raise PermissionDenied("You do not have permission to add a portfolio.")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, "Portfolio created successfully!")
        return super().form_valid(form)
    

@method_decorator(login_required, name='dispatch')
class UpdatePortfolioView(UpdateView):
    model = Portfolio
    fields = ['name', 'description', 'img', 'link']
    template_name = 'portfolio/updateportfolio.html'
    success_url = '/portfolio/'