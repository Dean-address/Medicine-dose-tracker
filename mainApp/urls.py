from django.urls import path
from . import views

app_name = "mainApp"
urlpatterns = [
    path("dashboard/<str:username>", views.index, name="index"),
    path("logout", views.logout_user, name="logout_user"),
    path("profile/<str:username>", views.show_new_form, name="show_new_form"),
    path("dosage_created", views.create_dosage, name="create_dosage"),
    path("delete/<int:dosage_id>", views.delete_dosage, name="delete_dosage"),
    path("edit/<int:dosage_id>/", views.edit_dosage, name="edit_dosage"),
]
