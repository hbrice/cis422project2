from django.db import models
from django.contrib.auth.models import User
from datetime import datetime.datetime as datetime


MONDAY = 'M'
TUESDAY = 'T'
WEDNESDAY = 'W'
THURSDAY = 'TH'
FRIDAY = 'F'
SATURDAY = 'S'
SUNDAY = 'SU'
AVAIL_DAY_CHOICES = ((MONDAY, 'M'),
	(TUESDAY, 'T'), (WEDNESDAY, 'W'),
	(THURSDAY, 'TH'), (FRIDAY, 'F'),
	(SATURDAY, 'S'), (SUNDAY, 'SU'))

class Employee(models.Model):
	user = models.ForeignKey(User, unique=True)
	company = models.CharField(max_length=100)
	isManager = models.BooleanField(default=False)
	setAvailibity = models.BooleanField(default=False)

	def  __unicode__(self):
		name = self.user.first_name + ' ' + self.user.last_name
		work = name + ' works for ' + self.company + ' and is a Manager ' + str(self.isManager)
		avail =  ' and has set there availibity ' + str(self.setAvailibity)
		output = work + '\n' + avail
		return output
		
	#The following functions are only applicable if Employee is a Manager
	def selectEmployee(self, emp):
		"""
			Employee emp: Employee to select
		"""
		clearSchedules()
		
	def unselectEmployee(self, emp):
		"""
			Employee emp: Employee to deselect
		"""
		clearSchedules()
	def activateEmployee(self, emp):
		"""
			Employee emp: Employee to activate
		"""
	
	def deactivateEmployee(self, emp):
		"""
			Employee emp: Employee to deactivate
		"""
		
	def addCoverage(self, times):
		"""
			DateTimeRange times: times to add to coverage
		"""
		clearSchedules()
	def removeCoverage(self, times):
		"""
			DateTimeRange times: times to remove from coverage
		"""
		clearSchedules()
	def clearSchedules(self):
		"""
			removes list of potential schedules and clears the best schedule
		"""
		self.bestSchedule = None
		self.potentialSchedules = []

class Availibity(models.Model):
	user = models.ForeignKey(User)
	AvailibleDay = models.CharField(max_length=2, choices=AVAIL_DAY_CHOICES)
	start_time = models.TimeField('Start Time')
	end_time = models.TimeField('End Time')

	def __unicode__(self):
		name = self.user.first_name + ' ' + self.user.last_name
		avail = ' is availible ' + self.AvailibleDay + ' at ' + str(self.start_time) + ' to ' + str(self.end_time)
		return name + avail
		
	def __init__(self):
		"""
			initialize the 2 dimensional array of booleans
		"""
		
	def addTime(self, times):
		"""
			DateTimeRange times: range to be added to availability
		"""
		
	def removeTime(self, times):
		"""
			DateTimeRange times: range of times to be removed from availability
		"""
		
	def isAvailable(self, times):
		"""
			DateTimeRange times: range of times to compare against availability
			returns whether all time in times is available
		"""


class Schedule(models.Model):
	user = models.ForeignKey(User)
	AvailibleDay = models.CharField(max_length=2, choices=AVAIL_DAY_CHOICES)
	start_time = models.TimeField('Start Time')
	end_time = models.TimeField('End Time')
	monthForSched = models.DateField('month created', auto_now_add=True)
	
	def addShift(self, employee, times):
		"""
			Employee employee: employee to add to shift
			DateTimeRange times: time employee will be sheduled
			
			add an association of employees and times to shifts
			#TODO up to the implementer maybe a tuple containing the association object.
		"""

	
class DateTimeRange:
	def __init__(self, sYear,sMonth,sDay,sHour,eYear,eMonth,eDay,eHour):
		start = datetime(sYear,sMonth,sDay,sHour)
		end = datetime(eYear,eMonth,eDay,eHour)
	def isDisjoint(self, otherRng):
		"""
			DateTimeRange otherRng: other DateTimeRange
			returns bool whether self and other are disjoint
		"""
		return ((self.start < otherRng.start) and (self.end < otherRng.start)) or ((otherRng.start < self.start) and (otherRng.end < self.start))
		
	def hours(self):
		"""
			returns a list of consequtive hours between start and end
		"""
		hours = []
		diff = end - start
		diff = diff.total_seconds() / 3600 # seconds / 3600 ==> hours
		
		while(diff > 0):
			hours.append(hours--)
		
		return hours