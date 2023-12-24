from dataclasses import dataclass
from collections import deque
from functools import wraps
from enum import Enum
from typing import List
import time

prime_it = lambda coro: wraps(coro)(lambda *a, **kw: [ci := coro(*a, **kw), next(ci)][0])

@dataclass
class Employee:
    Id: int = None
    available: bool = True

    next_id = 1

    def __post_init__(self):
        if self.Id is None:
            self.Id = Employee.next_id
            Employee.next_id += 1

        self.phone = self.telephone()

    def busy(self) -> None:
        self.available = False

    def is_available(self) -> None:
        self.available = True

    @prime_it
    def telephone(self):
        identity = f'{self.__class__.__name__}: {self.Id}'
        while True:
            try:
                call = (yield)
                if call and isinstance(call, Call):
                    print(f"{identity} answered the call. Caller: {call.caller_name}")
                    self.busy()
                    time.sleep(.5)
                    call.resolved = self.can_resolve(call)

                    if call.resolved: print("Call ended.")
                    else: print("Call could not be resolved. Needs escalation.")
                    self.is_available()
            except GeneratorExit:
                print(f"{identity} Accepting no more calls")
                return

class Severity(Enum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2

@dataclass
class Call:
    caller_name: str
    severity: Severity
    resolved: bool = False

    def assign(self, callee: Employee):
        callee.phone.send(self)

class Operator(Employee):
    def can_resolve(self, call: Call):
        return call.severity in [Severity.LOW]

class Supervisor(Employee):
    def can_resolve(self, call: Call):
        return call.severity in [Severity.LOW, Severity.MEDIUM]

class Director(Employee):
    def can_resolve(self, call: Call):
        return True

class CallCenter:
    def __init__(self, operators, supervisors, directors):
        self.operators = [Operator() for _ in range(operators)]
        self.supervisors = [Supervisor() for _ in range(supervisors)]
        self.directors = [Director() for _ in range(directors)]

        self.queue = deque()

    def dispatch(self, call: Call) -> None:
        if not call.resolved:
            self._transfer(call, self.operators)
        
        # call could not be resolved by operator or there were no operators available
        if not call.resolved:
            self._transfer(call, self.supervisors)

        # call could not be resolved by supervisor or there were no supervisors available
        if not call.resolved:
            self._transfer(call, self.directors)

        self.queue.append(call)
    
    def _transfer(self, call: Call, employees: List[Employee]):
        for employee in employees:
            if employee.available:
                call.assign(employee)
