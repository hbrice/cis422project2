from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from lunarshiftapp.models import Employee, Availibity, Schedule
from django.core.exceptions import ObjectDoesNotExist
from django.core.context_processors import csrf

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
						return redirect("/manager/" + username)
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

def signout_view(request):
	logout(request)
	return redirect("/")

@login_required(login_url='/')	
def home_view(request, employee_type, username):
	e = Employee.objects.get(user__username=username)
	context = {'name': e.user.first_name + " " + e.user.last_name, 'company': e.company}
	if (employee_type == "manager"):
		if e.isManager:
			scheduled = []
			for i in Employee.objects.filter(isManager=False):
				tmp = Schedule.objects.filter(user__username=i.user.username)
				if len(tmp) > 0:
					scheduled.append(i.user.username)

			context = {'name': e.user.first_name + " " + e.user.last_name, 
									'username': e.user.username,
									'company': e.company, 'employees': Employee.objects.filter(isManager=False),
									'scheduled': scheduled, 'hoursToCover': Availibity.objects.filter(user__username=e.user.username)}
			return render(request, 'manager.html', context)
	else:
		if e.isManager == False:
			if request.method=="POST" and request.is_ajax():
				available=Availibity(user=e.user,AvailibleDay='T',start_time='16:18:50',end_time='16:18:51')
				available.save()
				return HttpResponse('It worked!')
		
			#return HttpResponse('You are a employee')
			c = {}
			#c.update(csrf(request))
			#context = csrf(request)
			context["scheduledHours"] = Schedule.objects.filter(user__username=e.user.username)
                        context["days"] = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
			context["currentAvailability"] = Availibity.objects.filter(user__username=e.user.username)		
			context["username"] = e.user			
			#return render_to_response('employee.html', context)
			return render(request, 'employee.html', context)

def about_view(request):
	return render(request, 'about.html')

def contact_view(request):
	return render(request, 'contact.html')

def delete_view(request):
	return HttpResponse("Delete button pressed...")

def updateSlider_view(request):
	if request.method == 'POST' and request.is_ajax():
		day = request.POST['day']
		username = request.POST['username']
		startTime = request.POST['newStartTime']
		endTime = request.POST['newEndTime']
		newAv = Availibity.objects.get(user__username=username, AvailibleDay=day)
		newAv.start_time = str(startTime) + ":00"
		newAv.end_time = str(endTime) + ":00"
		newAv.save()
		return HttpResponse("")
		# user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
		#return HttpResponse("IT FUCKING WORKS! " + username + " " + day + " " + startTime + " " + endTime)

def submitAvailability_view(request):
	if request.method == 'POST' and request.is_ajax():
		day = request.POST['day']
		username = request.POST['username']
		startTime = request.POST['newStartTime']
		endTime = request.POST['newEndTime']
		availability = Availibity.objects.get(user__username=username,AvailibleDay=day)
		availability.start_time = startTime+":00:00"
		availability.end_time = endTime+":00:00"
		availability.save()

		return HttpResponse( username + " " + day + " " + startTime + " " + endTime)
		


