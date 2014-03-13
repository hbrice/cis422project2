import models
from models import Employee, Availibity, Schedule
from datetime import time

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
