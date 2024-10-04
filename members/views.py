
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import *
from django.shortcuts import render, redirect
from .forms import MemberCreationForm


# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = MemberCreationForm(request.post)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            login(request, user)
            return request('/')
    else:
        form = MemberCreationForm()
    return render(request, 'registeruser.html', {'form': form})
    