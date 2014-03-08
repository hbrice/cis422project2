from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from lunarshiftapp.models import Employee, Availibity, Schedule

# mainly for testing routing using
from django.http import HttpResponse

# Create your views here.
def index(request, auth_form=None, user_form=None):
	return render(request,'login.html')
	# This was for testing
	# return HttpResponse("This is where the signup page will be...")

def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				# redirect to user page...successful login
				tmp = email + " " + password		
				return HttpResponse("login worked!")
			else:
				# return a disabled account error message
				return HttpResponse("Error: disabled account")
		else:
			# invalid username/ password
			return HttpResponse("username or password is incorrect")
		
	

'''
This will break code since url aren't defined yet...to do later
def employee(request, user_id):
	return HttpResponse("This is where the employee page will be for " % employee_id)

def mananger(request, user_id):
	return HttpResponse("This is where the manager page will be for " % employee_id))'''
    