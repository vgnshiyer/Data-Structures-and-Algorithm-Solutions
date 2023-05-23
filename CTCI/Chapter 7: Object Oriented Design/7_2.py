class Employee:
    isAvailable = True
    rank = -1

    def __init__(self, name, age, rank):
        self.name = name
        self.age = age
        self.rank = rank

    def level(self):
        if self.rank == 3:
            return 'Respondent'
        elif self.rank == 2:
            return 'Manager'
        else:
            return 'Director'

class Respondent(Employee):
    def __init__(self, name, age):
        super().__init__(name, age, 3)

class Manager(Employee):
    def __init__(self, name, age):
        super().__init__(name, age, 2)

class Director(Employee):
    def __init__(self, name, age):
        super().__init__(name, age, 1)

class Call:
    placed = False
    queueNumber = -1

    def assignHandler(self, emp: Employee):
        self.handler = emp

    def printStatus(self):
        if self.placed:
            print('Call has been assigned to {0} who is a {1}'.format(self.handler.name, self.handler.level()))
        else:
            print('Your are at position {0} in the queue. A representative will attend your call soon.'.format(self.queueNumber))

    def end(self):
        self.handler.isAvailable = True
        return self.handler

class CallHandler:
    availableRespondents = []
    availableManagers = []
    availableDirectors = []

    callQueue = []

    def addEmployee(self, emp: Employee):
        if emp.rank == 3:
            self.availableRespondents.append(emp)
        elif emp.rank == 2:
            self.availableManagers.append(emp)
        else:
            self.availableDirectors.append(emp)

        if self.callQueue:
            self.assignCall(self.callQueue.pop(0))

    def assignCall(self, call):
        emp = self.getNextAvailableAttendant()
        if not emp:
            ## place call in queue
            self.callQueue.append(call)
            call.queueNumber = len(self.callQueue)
            call.printStatus()
        else:
            call.placed = True
            call.handler = emp
            emp.isAvailable = False
            call.printStatus()

    def getNextRespondent(self) -> Respondent:
        return self.availableRespondents.pop()

    def getNextManager(self) -> Manager:
        return self.availableManagers.pop()

    def getNextDirector(self) -> Director:
        return self.availableDirectors.pop()
    
    def getNextAvailableAttendant(self) -> Employee:
        if self.availableRespondents:
            return self.getNextRespondent()
        elif self.availableManagers:
            return self.getNextManager()
        elif self.availableDirectors:
            return self.getNextDirector()
        else:
            return None

if __name__ == '__main__':
    handler = CallHandler()
    handler.addEmployee(Respondent('respondent1', '21'))
    handler.addEmployee(Respondent('respondent2', '22'))
    handler.addEmployee(Respondent('respondent3', '24'))

    handler.addEmployee(Manager('manager1', '31'))
    handler.addEmployee(Manager('manager2', '31'))
    handler.addEmployee(Manager('manager3', '32'))

    handler.addEmployee(Director('director1', '41'))
    handler.addEmployee(Director('director2', '41'))
    handler.addEmployee(Director('director3', '44'))

    call = Call()
    handler.assignCall(call)
    emp = call.end()