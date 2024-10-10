from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from authApp.forms import LoginForm, SignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login



# Create your views here.
def sign_up(request):
    sigup_form = SignupForm()
    return render(request, 'signup.html', {'form':sigup_form})

def log_in(request):
    login_form = LoginForm()
    return render(request, 'login.html', {'form':login_form})

# logic for saving user to admin
def register_user(request):
    if request.method == 'POST':
      first_name = request.POST['first_name']
      last_name = request.POST['last_name']
      email = request.POST['email']
      password = request.POST['password']
    
    new_user = User.objects.create_user(username=f'{first_name+last_name}', email=email, password=password, first_name=first_name, last_name=first_name)
    
    if new_user:
        return redirect('authApp:login')
    else:
     sigup_form = SignupForm()
    return render(request, 'signup.html', {'form':sigup_form})

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
        
    user = authenticate(request,username=username, password=password)
    
    if user is not None:
        login(request, user)
        return redirect('mainApp:index', username=username)
    else:
        login_form = LoginForm()
        return render(request, 'login.html', {'error_message':'Invalid Credit', 'form':login_form}, )
    


    
        
        
        
