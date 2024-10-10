from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse

# Create your views here.
@login_required(login_url='authApp:login')
def index(request, username):
    return render(request, 'index.html',{})

def logout_user(request):
    logout(request)
    return redirect('authApp:login')
    