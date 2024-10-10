from django.urls import path
from . import views
app_name='mainApp'
urlpatterns=[
	path('dashboard/<str:username>',views.index, name='index' ),
	path('logout', views.logout_user, name='logout_user'),
]