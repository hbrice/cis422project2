from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from lunarshiftapp.models import Employee, Availibity, Schedule
from lunarshuftapp.functionality import DateTimeRange
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
									'scheduled': scheduled, 'hoursToCover': Availibity.objects.filter(user__username=e.user.username),
									'schedules': Schedule.objects.all()}
			return render(request, 'manager.html', context)
	else:
		if e.isManager == False:		
			c = {}
			context["scheduledHours"] = Schedule.objects.filter(user__username=e.user.username)
                        context["days"] = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
			context["currentAvailability"] = Availibity.objects.filter(user__username=e.user.username)		
			context["username"] = e.user
			return render(request, 'employee.html', context)

def addEmployee(request):
	if request.method == 'POST' and request.is_ajax():
		username = request.POST['username']
		firstname = request.POST['firstname']
		lastname = request.POST['lastname']
		password = request.POST['password']

		e = Employee.objects.get(isManager=True)
		u = User(
			username = username,
			first_name = firstname,
			last_name = lastname, 
			password = password
		)
		u.save()
		newE = Employee(user=u, company=e.company)
		newE.save()
		return HttpResponse()

def deleteEmployee(request):
	if request.method == 'POST' and request.is_ajax():
		username = request.POST['username']
		e = Employee.objects.get(user__username=username)
		u = User.objects.get(username=username)
		e.delete()
		u.delete()
	return HttpResponse()

def deleteDayToCover(request):
	if request.method == 'POST' and request.is_ajax():
		day = request.POST['day']
		manager = Employee.objects.get(isManager=True)
		a = Availibity.objects.get(user__username=manager.user.username, AvailibleDay=day)
		a.delete()
		return HttpResponse()

def about_view(request):
	return render(request, 'about.html')

def contact_view(request):
	return render(request, 'contact.html')

def delete_view(request):
	return HttpResponse("Delete button pressed...")

def updateAvailibility(request):
	if request.method == 'POST' and request.is_ajax():
		day = request.POST['day']
		username = request.POST['username']
		startTime = request.POST['newStartTime']
		endTime = request.POST['newEndTime']
		newAv = Availibity.objects.get(user__username=username, AvailibleDay=day)
		newAv.start_time = str(startTime) + ":00"
		newAv.end_time = str(endTime) + ":00"
		newAv.save()
		return HttpResponse()

'''
def calculateSchedule(request):
	if request.method == 'POST' and request.is_ajax():
		employeesSet = request.POST['employees']
		manager = request.POST['manager']
		#daysNeedingCoverage return a list of Schedule records, each representing a day that needs coverage
		daysNeedingCoverage = Availibity.objects.get(user__username=manager) # manager availability is coverage	
		#store the number of days that are in the schedule
		numberOfdays = daysNeedingCoverage.length
		#variable to store the number of hour chunks needing to be covered
		numberofHours = 0;
		#variable for returning messages (testing)
		returnMsg = ""


		#loop through each day that has coverage
		for day in daysNeedingCoverage
			#loop through each hour of coverage in the day
			for hour in range(day.start_time, day.end_time)
				#get the number of total hours in the schedule that need coverage
				numberOfHours += 1
				#get the set of employees who can cover this hour
				poolOfEmployees=Availibity.objects.get(interval.AvailibleDay=day, start_time<=hour<=end_time))
		


	return HttpResponse(returnMsg)
'''





			
			
		
		



