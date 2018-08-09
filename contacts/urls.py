from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'contacts'

urlpatterns = [
	path('mycontacts/', views.mycontacts, name='mycontacts'),
	path('add_contact/', views.add_contact, name='add_contact'),
	path('register/', views.register, name='register'),
	path('login/', views.login, name='login'),
	path('logout/', views.logout, name='logout'),
]