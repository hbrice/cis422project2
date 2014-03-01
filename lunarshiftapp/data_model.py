from datetime import datetime.datetime as datetime

class DateTimeRange:
	def __init__(self, sYear,sMonth,sDay,sHour,eYear,eMonth,eDay,eHour):
		start = datetime(sYear,sMonth,sDay,sHour)
		end = datetime(eYear,eMonth,eDay,eHour)
	def isDisjoint(self, otherRng):
		"""
			DateTimeRange otherRng: other DateTimeRange
			returns bool whether self and other are disjoint
		"""
		
	def hours(self):
		"""
			returns a list of consequtive hours between start and end
		"""
		
	
class Employee:
	def __init__(self, fName, lName, company, email):
	"""
		String fName: first name
		String lName: last name
		String company: company name
		String email: employee email
	"""
		self.fName = fName
		self.lName = lName
		self.company = company
		self.email = email
	
class Manager:
	def __init__(self, info, allEmployees):
	"""
		Employee info: Managers information
		Employee{} allEmployees: set off all managers employees
	"""
	
		self.managerInformation = info
		self.allEmployees = allEmployees
	
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
		
	def computeSchedules(self):
		"""
			attempts to create list of potential schedules using resources. Then selects the most appropriate schedule as best
		"""
		clearSchedules()
	
	


