from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from members.decorators import allowed_users
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
    context_object_name = 'portfolio'

class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio_detail.html'

@method_decorator(login_required, name='dispatch')
@method_decorator(allowed_users(allowed_roles=['Admin']), name="dispatch")
class AddPortfolioView(CreateView):
    model = Portfolio
    form_class = PortfolioForm
    template_name = 'add_portfolio.html'
    success_url = reverse_lazy('portfolio:portfolio_list')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def handle_no_permission(self):
        raise PermissionDenied("You do not have permission to add a portfolio.")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, "Portfolio created successfully!")
        return super().form_valid(form)
    

@method_decorator(login_required, name='dispatch')
@method_decorator(allowed_users(allowed_roles=['Admin']), name="dispatch")
class EditPortfolioView(UpdateView):
    model = Portfolio
    form_class = PortfolioForm
    template_name = 'portfolio_edit.html'
    success_url = reverse_lazy('portfolio:portfolio_list')

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_superuser or self.request.user.groups.filter(name='Admin').exists():
            return queryset
        return queryset.filter(created_by=self.request.user) | queryset.filter(created_by__isnull=True)
    
    def get_success_url(self):
        return reverse('portfolio:portfolio_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
@method_decorator(allowed_users(allowed_roles=['Admin']), name="dispatch")
class DeletePortfolioView(DeleteView):
    model = Portfolio
    template_name = 'portfolio_delete.html'
    success_url = reverse_lazy('portfolio:portfolio_list')

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_superuser or self.request.user.groups.filter(name='Admin').exists():
            return queryset
        return queryset.filter(created_by=self.request.user) | queryset.filter(created_by__isnull=True)

   