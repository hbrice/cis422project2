from django.db import models
from django.contrib.auth.models import User

MONDAY = 'M'
TUESDAY = 'T'
WEDNESDAY = 'W'
THURSDAY = 'TH'
FRIDAY = 'F'
SATURDAY = 'S'
SUNDAY = 'SU'
AVAIL_DAY_CHOICES = ((MONDAY, 'Monday'),
	(TUESDAY, 'Tuesday'), (WEDNESDAY, 'Wednesday'),
	(THURSDAY, 'Thursday'), (FRIDAY, 'Friday'),
	(SATURDAY, 'Saturday'), (SUNDAY, 'Sunday'),
	)

class Employee(models.Model):
	"""
		user: django user field consisting of a username and password.
		company: String holding company name
		isManager: bool flag for manager identification.
		setAvailaibility: bool flag if availability has been added for a user.
	"""
	user = models.ForeignKey(User, unique=True)
	company = models.CharField(max_length=100)
	isManager = models.BooleanField(default=False)
	setAvailibity = models.BooleanField(default=False)
	
	
		
	def  __unicode__(self):
		"""
		logic describing how an Employee object will be represented as a string.
		"""
		name = self.user.first_name + ' ' + self.user.last_name
		work = name + ' works for ' + self.company + ' and is a Manager ' + str(self.isManager)
		avail =  ' and has set there availibity ' + str(self.setAvailibity)
		output = work + '\n' + avail
		return output

class Availibity(models.Model):
	"""
		user: user associated with the availability entry
		AvailableDay: max 2 character string for day abbreviation
		start_time: The start of the availability
		end_time: The end of the availability
	"""
	user = models.ForeignKey(User)
	AvailibleDay = models.CharField(max_length=2, choices=AVAIL_DAY_CHOICES)
	start_time = models.TimeField('Start Time')
	end_time = models.TimeField('End Time')

	def __unicode__(self):
		"""
		String representation of Availability
		"""
		name = self.user.first_name + ' ' + self.user.last_name
		avail = ' is availible ' + self.AvailibleDay + ' at ' + str(self.start_time) + ' to ' + str(self.end_time)
		return name + avail
		
	


class Schedule(models.Model):
	"""
		user: the user associated with a schedule.
		AvailableDay
		start_time
		end_time
		monthForSched
	"""
	user = models.ForeignKey(User)
	AvailibleDay = models.CharField(max_length=2, choices=AVAIL_DAY_CHOICES)
	start_time = models.TimeField('Start Time')
	end_time = models.TimeField('End Time')
	monthForSched = models.DateField('month created', auto_now_add=True)
	


	
