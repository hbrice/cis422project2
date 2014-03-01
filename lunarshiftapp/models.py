from django.db import models
from django.contrib.auth.models import User

"""
Employee Inherits from User:
1. Instantiate a new employee consisting of a first name, last name, employeeID, email address, and a list of available times	
2. Add and remove available dates from the list of available time.
"""
class Employee(models.Model):
	manager = models.ForeignKey(Manager)
	company = models.CharField(max_length=100)
	user = models.ForeignKey(User, unique=True)
        
        #Adds the DateTimeRange object to the list previously created by the Employee __init__ method.
        def addTime(rng):

        #Removes the DateTimeRange object at position index of the list of available times.
        def removeTime(rng):

class Manager(models.Model):	
	company = models.CharField(max_length=100)
	user = models.ForeignKey(User, unique=True)

class Schedules(models.Model):
	userID = models.ForeignKey(User, unique=True)
	start = models.CharField(max_length=6) #format HR:DAY
	end = models.CharField(max_length=6) #format HR:DAY
	scheduleID = models.IntegerField(default=0)

class Availability(models.Model):
	userID = models.ForeignKey(User, unique=True)
	start = models.CharField(max_length=6) #format HR:DAY
	end = models.CharField(max_length=6) #format HR:DAY
	isAvailable = models.BooleanField(initial=True)

