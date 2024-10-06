from django.shortcuts import render
from django.http import HttpResponse
from authApp.forms import LoginForm, SignupForm
# Create your views here.

def sign_up(request):
    signp_form = SignupForm()
    return render(request, 'signup.html', {'form':signp_form})

def log_in(request):
    login_form = LoginForm()
    return render(request, 'login.html', {'form':login_form})