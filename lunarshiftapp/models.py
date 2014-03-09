from django.db import models
from django.contrib.auth.models import User

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
		
	#The following fuctions are only applicable if Employee Manager
	def selectEmployee(self, emp):
		"""
			Employee emp: Employee to select
		"""
		computeSchedules()
		
	def unselectEmployee(self, emp):
		"""
			Employee emp: Employee to deselect
		"""
		computeSchedules()
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
		computeSchedules()
	def removeCoverage(self, times):
		"""
			DateTimeRange times: times to remove from coverage
		"""
		computeSchedules()
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

class Schedule(models.Model):
	user = models.ForeignKey(User)
	AvailibleDay = models.CharField(max_length=2, choices=AVAIL_DAY_CHOICES)
	start_time = models.TimeField('Start Time')
	end_time = models.TimeField('End Time')
	monthForSched = models.DateField('month created', auto_now_add=True)
