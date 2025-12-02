from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Portfolio
from django.shortcuts import render, redirect
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
    fields = ['title', 'description', 'image', 'link']
    template_name = 'portfolio/addportfolio.html'
    success_url = '/portfolio/'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
    def handle_no_permission(self):
        raise PermissionDenied("You do not have permission to add a portfolio item.")
    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, "Portfolio item created successfully!")
        return super().form_valid(form)
    

@method_decorator(login_required, name='dispatch')
class UpdatePortfolioView(UpdateView):
    model = Portfolio
    fields = ['title', 'description', 'image', 'link']
    template_name = 'portfolio/updateportfolio.html'
    success_url = '/portfolio/'

    def dispatch(self, request, *args, **kwargs):
        portfolio = self.get_object()
        if portfolio.owner != request.user:
            raise PermissionDenied("You do not have permission to edit this portfolio item.")
        return super().dispatch(request, *args, **kwargs)