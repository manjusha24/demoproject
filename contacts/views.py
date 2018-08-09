from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Contact
from .forms import CustomUserCreationForm, CustomContactCreationForm
# Create your views here.

def mycontacts(request):
	if not request.user.is_authenticated:
		return redirect('contacts:login')

	contacts_list = Contact.objects.filter(user=request.user)
	context = {'contacts_list': contacts_list}
	return render(request, 'contacts/index.html', context)

def add_contact(request):
	if not request.user.is_authenticated:
		return redirect('contacts:login')

	if request.method == 'POST':
		form = CustomContactCreationForm(request.POST)
		if form.is_valid():
			contact = form.save(commit=False)
			contact.user = request.user
			contact.save() 
			messages.success(request, 'Contact added successfully')
			return redirect('contacts:mycontacts')

	else:
		form = CustomContactCreationForm()

	return render(request, 'contacts/add_contact.html', {'form': form})

def login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = auth.authenticate(username=username, password=password)

		if user is not None:
			# correct username and password login the user
			auth.login(request, user)
			return redirect('contacts:mycontacts')

		else:
			messages.error(request, 'Error wrong username/password')

	return render(request, 'contacts/login.html')

def logout(request):
	if not request.user.is_authenticated:
		messages.error(request, 'You are already logged out')
		return redirect('contacts:login')

	auth.logout(request)
	return render(request,'contacts/logout.html')

def register(request):
	if request.method == 'POST':
		f = CustomUserCreationForm(request.POST)
		if f.is_valid():
			f.save()
			messages.success(request, 'Account created successfully')
			return redirect('contacts:login')

	else:
		f = CustomUserCreationForm()

	return render(request, 'contacts/register.html', {'form': f})
