from django.shortcuts import render
import json
from datetime import datetime
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.contrib.auth import logout, authenticate, views as auth_views, login as log_in
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .forms import RegistrationForm, UserLoginForm
from .models import UserBase

def register(request):

    if request.user.is_authenticated:
        return redirect('hist_app:list_view')

    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)

        if registerForm.is_valid():

            # Create user

            password = registerForm.cleaned_data['password']
            user = registerForm.save(commit=False)
            user.user_name = registerForm.cleaned_data['email'].split('@')[0]
            user.email = registerForm.cleaned_data['email']
            user.set_password(password)
            user.is_active = True
            user.save()

        else:
            HttpResponse("Error handler content", status=400)

    else:
        registerForm = RegistrationForm()

    return render(request, 'auth_app/register.html', {'form': registerForm})

def login (request):
    if request.user.is_authenticated:
        return redirect('hist_app:list_view')

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active and user.is_authenticated:
            log_in(request, user)
            return redirect('hist_app:list_view')
        else:
            messages.error(request, 'Invalid email or password')
            return render(request, 'auth_app/login.html', {'form': UserLoginForm})
    else:
        return render(request, 'auth_app/login.html', {'form': UserLoginForm})