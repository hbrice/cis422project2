import models
from models import Employee, Availibity, Schedule
from datetime import time

#probably don't need these anymore.
MONDAY = models.MONDAY
TUESDAY = models.TUESDAY
WEDNESDAY = models.WEDNESDAY
THURSDAY = models.THURSDAY
FRIDAY = models.FRIDAY
SATURDAY = models.SATURDAY
SUNDAY = models.SUNDAY


#The following functions are only applicable if Employee is a Manager
def addEmployee(self, usrName, pw, cmpny, manager=False):
	"""
	usrName: string to add as the username
	pw: string signifying the password
	cmpny: string to add a company to an employee
	"""
	u = User(username=usrName, password=pw)
	u.save()
	emp = Employee(user=u, company=cmpny, isManager=manager)
	emp.save()
	
def removeEmployee(self, usrName):
	"""
	usrName an employees username who will be removed from the database.
	"""
	Employee.objects.get(username=usrName).delete()
	
def addCoverage(self, times):
	"""
		DateTimeRange times: times to add to coverage
	"""
	
	
def removeCoverage(self, times):
	"""
		DateTimeRange times: times to remove from coverage
	"""
		
		
		
#Availability
	
def addTime(self, times):
	"""
		DateTimeRange times: range to be added to availability
	"""
	pass
	
def removeTime(self, times):
	"""
		DateTimeRange times: range of times to be removed from availability
	"""
	pass
	
def isAvailable(self, times):
	"""
		DateTimeRange times: range of times to compare against availability
		returns whether all time in times is available
	"""
	
	
#Schedule
def addShift(self, employee, times):
	"""
		Employee employee: employee to add to shift
		DateTimeRange times: time employee will be sheduled
		
		add an association of employees and times to shifts
		#TODO up to the implementer maybe a tuple containing the association object.
	"""
	pass
#
class DateTimeRange:
	def __init__(self, day, start, end):
		"""
			day is a string as defined above for the day.
			start and end can be either integers(representing hours) or time objects.
			creates tuple self.time (day, start, end)
		"""
		startTime = datetime.time(start)
		endTime = datetime.time(end)
		self.time = (day,startTime,endTime)
	
	def isDisjoint(self, otherRng):
		"""
			DateTimeRange otherRng: other DateTimeRange
			returns bool whether self and other are disjoint
		"""
		return self.time[0] != otherRng.time[0] or ((self.time[1] < otherRng.time[1]) and (self.time[2] < otherRng.time[1])) or ((otherRng.time[1] < self.time[1]) and (otherRng.time[2] < self.time[1]))
		
	def hours(self):
		"""
			returns a list of consecutive hours between start and end
		"""
		return List(range(self.time[1].hour,self.time[2].hour + 1))
