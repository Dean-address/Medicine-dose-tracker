from django.urls import path
from . import views
app_name = 'authApp'
urlpatterns = [
	path('signup/',views.sign_up, name='signup' ),
	path('login/', views.log_in, name='login'),
	path('signup_success/', views.register_user, name='register_user'),
	path('login', views.authenticate_user, name='authenticate_user'),
]