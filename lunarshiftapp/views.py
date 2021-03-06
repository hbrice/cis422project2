from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from lunarshiftapp.models import Employee, Availibity, Schedule
from django.core.exceptions import ObjectDoesNotExist
from django.core.context_processors import csrf
from django.contrib.auth.hashers import make_password
from lunarshiftapp.functionality import *

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
			context = {'name': e.user.first_name + " " + e.user.last_name, 
									'username': e.user.username,
									'company': e.company, 
									'hoursToCover': Availibity.objects.filter(user__username=e.user.username),
									'schedules': Schedule.objects.all()}
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
			password = make_password(password)
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
		username = request.POST['username']
		a = Availibity.objects.get(user__username=username, AvailibleDay=day)
		a.delete()
		'''try:
			tmp = Availibity.objects.get(user__username=username)
		except ObjectDoesNotExist:
			e = Employee.objects.get(user__username=username)
			e.setAvailibity = False
			e.save()'''
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

def addTime(request):
	if request.method == 'POST' and request.is_ajax():
		day = request.POST['day']
		username = request.POST['username']
		u = User.objects.get(username=username)
		e = Employee.objects.get(user__username=username)
		if e.setAvailibity == False:
			e.setAvailibity = True
		e.save()
		newAv = Availibity(
			user = u,
			AvailibleDay = day,
			start_time = "8:00",
			end_time = "17:00",
		)
		newAv.save()
		return HttpResponse()

def computeSchedule(request):
	if request.method == 'POST' and request.is_ajax():
		employeesSet = request.POST['employees']
		manager = request.POST['manager']
		#daysNeedingCoverage return a list of Schedule records, each representing a day that needs coverage
		daysNeedingCoverage = Availibity.objects.filter(user__username=manager) # manager availability is coverage	
		Schedule.objects.all().delete()
			
		#store the number of days that are in the schedule
		numberOfdays = len(Availibity.objects.filter(user__username=manager))
		#variable to store the number of hour chunks needing to be covered
	
		#return HttpResponse(numberOfdays)
		#variable for returning messages (testing)
		returnMsg = ""
		numberOfHours = 0
		poolCounter = 0
		managerCounter = 0
		#loop through each day that has coverage
		for day in daysNeedingCoverage:
			#return HttpResponse(day)
			#loop through each hour of coverage in the day
			for hour in range(day.start_time.hour, day.end_time.hour):
				#get the number of total hours in the schedule that need coverage
				numberOfHours += 1
				poolOfEmployees = []
				returnUsers = ""
				#get the set of employees who can cover this hour
				a = Availibity.objects.filter(AvailibleDay=day.AvailibleDay)#.exclude(user__username="test")
				for e in a:
					if e.start_time.hour<= hour:
						#if  len(Employee.objects.filter(user=e.user,isManager=True)) > 0:						
						#if e.user.username=='test':
						#	managerCounter += 1
							#return HttpResponse(e.user)
						#else:
								#returnUsers += str(e.user) + ","
							if str(e.user)!="test":
								poolOfEmployees.append(e)
								poolCounter += 1
				#poolOfEmployees =  Availibity.objects.filter(AvailibleDay=day.AvailibleDay)
				tmpSet = employeesSet
				#return HttpResponse(Availibity.objects.filter(AvailibleDay=day).count())
				#for x in poolOfEmployees:
				#	if x.user not in tmpSet:
				#		tmpSet.remove(x)
				if len(tmpSet) == 0 or len(poolOfEmployees)==0:
					return HttpResponse("None " + str(managerCounter))
				else:		
					newStart = str(hour) + ":00" 
					newEnd = str(hour+1) + ":00" 
					newSchedule = Schedule(user=User.objects.get(username=poolOfEmployees[0].user),AvailibleDay=day.AvailibleDay,start_time=newStart,end_time=newEnd)
					newSchedule.save()
		return HttpResponse(str(poolCounter) + " " + str(managerCounter) + " " + str(returnUsers))
				
	return HttpResponse("No schedules!")


def altComputeSchedule(request):
	if request.method == 'POST' and request.is_ajax():
		employeesSet = request.POST['employees']
		manager = request.POST['manager']
		
		compute = ComputeSchedule(employeesSet,manager)
		compute.produceSchedules([],{'M':[],'T':[],'W':[],'TH':[],'F':[],'S':[],'SU':[]},compute.k)
	return HttpResponse("Schedules!")
