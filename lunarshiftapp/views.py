from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from models import Employee

def index(request):
	#return HttpResponse("This is where the signup page will be...")
	return render(request,'login.html')

'''
This will break code since url aren't defined yet...to do later
def employee(request, user_id):
	return HttpResponse("This is where the employee page will be for " % employee_id)

def mananger(request, user_id):
	return HttpResponse("This is where the manager page will be for " % employee_id))'''
    