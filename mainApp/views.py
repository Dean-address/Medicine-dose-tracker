from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import DosageForm
from .models import Dosage
from authApp.models import ProfilePic
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url="authApp:login")
def index(request, username):
    username = request.user
    dosages = Dosage.objects.filter(user=username)
    # a = dosages.username

    return render(
        request,
        "dosages_list.html",
        {"dosage": dosages},
    )


def logout_user(request):
    logout(request)
    return redirect("authApp:login")


def create_dosage(request):
    username = request.user

    if request.method == "POST":
        medicine_name = request.POST["medicine_name"]
        quantity = request.POST["quantity"]
        units = request.POST["units"]
        frequency = request.POST["frequency"]

    new_dosage = Dosage(
        user=username,
        medicine_name=medicine_name,
        quantity=quantity,
        units=units,
        frequency=frequency,
    )
    new_dosage.save()

    return redirect("mainApp:index", username=username)


@login_required(login_url="authApp:login")
def delete_dosage(request, dosage_id):
    username = request.user
    dosage = Dosage.objects.filter(pk=dosage_id)
    dosage.delete()
    return redirect("mainApp:index", username=username)


def edit_dosage(request, dosage_id):
    username = request.user
    # dosage = Dosage.objects.get(user=username)
    dosage = get_object_or_404(Dosage, id=dosage_id)
    if request.method == "POST":
        new_medicine_name = request.POST.get("editName")
        new_quantity = request.POST.get("editQuantity")
        new_units = request.POST.get("editUnit")
        new_frequency = request.POST.get("editFrequency")

        if new_medicine_name and new_quantity and new_units and new_frequency:
            dosage.medicine_name = new_medicine_name
            dosage.quantity = new_quantity
            dosage.units = new_units
            dosage.frequency = new_frequency
            dosage.save()
            return redirect("mainApp:index", username=request.user.username)
        else:
            return redirect("mainApp:index", username=request.user.username)

    return redirect("mainApp:index", username=username)


@login_required(login_url="authApp:login")
def show_new_form(request, username):
    form = DosageForm(username)
    return render(request, "index.html", {"form": form, "username": username})
