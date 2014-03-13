def nurseScheduling(Wanted, employeeInfo):
    candidates = scheduleCandidates(convertToShifts(Wanted), employeeInfo)
    return pickOne(candidates)

def isAvailable(employee, shift):
    i = 0
    for row in employee.availability:
        for column in employee.availability:
            if i = shift:
                return employee.availability[row][column]
            else:
                i = i + 1

def scheduleCandidates(shifts, employees):
    candidates = list()
    for shift in shifts:
        for employee in employees:
            if isAvailable(employee, shift):
                candidates.add((shift, employee))
    return candidates


    
