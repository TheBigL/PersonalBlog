from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Portfolio
from .forms import PortfolioForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
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
    form_class = PortfolioForm
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
class EditPortfolioView(UpdateView):
    model = Portfolio
    fields = ['name', 'description', 'img', 'link']
    template_name = 'portfolio/edit_portfolio.html'
    success_url = '/portfolio/'

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.filter(created_by=self.request.user)
    
    def get_success_url(self):
        return reverse('portfolio:portfolio_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class DeletePortfolioView(DeleteView):
    model = Portfolio
    template_name = 'portfolio/delete_portfolio.html'
    success_url = reverse_lazy('portfolio:portfolio_list')

    