from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from lunarshiftapp.models import Employee, Availibity, Schedule
from django.core.exceptions import ObjectDoesNotExist

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
				u = User.objects.get(username=username)
				try:
					e = Employee.objects.get(user=u)
					if e.isManager:
						return redirect("/mananger/" + username)
					else:
						return redirect("/employee/" + username)
				except ObjectDoesNotExist:
					return HttpResponse("This user is not assigned as an employee to a company")
			else:
				# return a disabled account error message
				return HttpResponse("Error: disabled account")
		else:
			# invalid username/ password
			return HttpResponse("username or password is incorrect")
		
def home_view(request, employee_type, username):
	u = User.objects.get(username=username)
	e = Employee.objects.get(user=u)
	context = {'name': u.first_name + " " + u.last_name, 'company': e.company}
	if (employee_type == "manager"):
		if e.isManager:
			return HttpResponse('you are a manager')
			#return render(request, 'base.html', context)
	else:
		if e.isManager == False:
			return HttpResponse('You are a employee')
			#return render(request, 'base.html', context)
