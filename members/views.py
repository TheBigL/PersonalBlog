
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from django.contrib.auth.forms import *
from django.urls import reverse_lazy
from .forms import MemberCreationForm
from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from .models import Member



# Create your views here.
class RegisterUser(CreateView):
    form = MemberCreationForm
    success_url = reverse_lazy('login')
    template_name = 'members/registeruser.html'
    success_message = "You have successfully registered!"

    def post(self, request, *args, **kwargs):
        pass
        form = MemberCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            group = Group.objects.get(name='Member')
            user.groups.add(group)
            return redirect('login')
        else:
            return render(request, 'registeruser.html', {'form': form})
        
class LoginUser(CreateView):
    form = AuthenticationForm
    template_name = 'loginuser.html'
    success_url = reverse_lazy('posts:post_list')

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})

            
