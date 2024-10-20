from django.shortcuts import redirect, render
from django.contrib.auth.models import User, Permission
from authApp.forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login
from .models import ProfilePic


# Create your views here.
def sign_up(request):
    sigup_form = SignupForm()
    return render(request, "signup.html", {"form": sigup_form})


def log_in(request):
    login_form = LoginForm()
    return render(request, "login.html", {"form": login_form})


# logic for saving user to admin
def register_user(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        #   pic = request.POST['profile_image']

        profile_image = request.FILES.get("profile_image")

    new_user = User.objects.create_user(
        username=f"{first_name+last_name}",
        email=email,
        password=password,
        first_name=first_name,
        last_name=first_name,
    )

    if new_user:
        permission1 = Permission.objects.get(codename="add_dosage")
        permission2 = Permission.objects.get(codename="view_dosage")
        permission3 = Permission.objects.get(codename="change_dosage")
        permission4 = Permission.objects.get(codename="delete_dosage")

        new_user.user_permissions.add(
            permission1, permission2, permission3, permission4
        )
        new_user.save()
    if profile_image:
        profile_pic = ProfilePic(user=new_user, image=profile_image)
    else:
        profile_pic = ProfilePic(user=new_user)

    if profile_pic:
        permission_add_pic = Permission.objects.get(codename="add_profilepic")
        permission_view_pic = Permission.objects.get(codename="view_profilepic")
        permission_change_pic = Permission.objects.get(codename="change_profilepic")
        permission_delete_pic = Permission.objects.get(codename="delete_profilepic")

        new_user.user_permissions.add(
            permission_add_pic,
            permission_change_pic,
            permission_view_pic,
            permission_delete_pic,
        )
        profile_pic.save()
        new_user.save()

        return redirect("authApp:login")
    else:
        sigup_form = SignupForm()
    return render(request, "signup.html", {"form": sigup_form})


def authenticate_user(request):
    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)

        return redirect("mainApp:index", username=username)
    else:
        login_form = LoginForm()
        return render(
            request,
            "login.html",
            {"error_message": "Invalid Credit", "form": login_form},
        )
