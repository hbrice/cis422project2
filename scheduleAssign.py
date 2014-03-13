def nurseScheduling(Wanted, employeeInfo):
    candidates = scheduleCandidates(convertToShifts(Wanted), employeeInfo)
    return pickOne(candidates)

def isAvailable(employee, shift):

def scheduleCandidates(shifts, employees):
    candidates = list()
    for shift in shifts:
        for employee in employees:
            if isAvailable(employee, shift):
                candidates.add((shift, employee))
    return candidates


    
