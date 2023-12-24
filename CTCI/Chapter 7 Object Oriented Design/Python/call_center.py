from dataclasses import dataclass
from collections import deque
from functools import wraps
from enum import Enum
from typing import List
import time, random, asyncio, datetime

class Severity(Enum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2

@dataclass
class Call:
    caller_name: str
    severity: Severity
    resolved: bool = False

@dataclass
class Employee:
    Id: int = None
    available: bool = True

    next_id = 1

    def __post_init__(self):
        if self.Id is None:
            self.Id = Employee.next_id
            Employee.next_id += 1

    def busy(self) -> None:
        self.available = False

    def is_available(self) -> None:
        self.available = True

    async def process_call(self, call: Call):
        identity = f'{self.__class__.__name__}: {self.Id}'
        print(f"{identity} answered the call. Caller: {call.caller_name}")
        self.busy()

        await asyncio.sleep(random.random()) # employee trying to resolve the call

        call.resolved = self.can_resolve(call)
        if call.resolved: 
            print("Call ended.")
        else: 
            print("Call could not be resolved. Needs escalation.")
        
        self.is_available()

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

    async def dispatch(self, calls: asyncio.Queue) -> None:
        while not calls.empty():
            call = await calls.get()

            if not call.resolved:
                await self._transfer(call, self.operators)

            if not call.resolved:
                await self._transfer(call, self.supervisors)
            
            if not call.resolved:
                await self._transfer(call, self.directors)

            if call.resolved:
                calls.task_done()

    async def _transfer(self, call: Call, employees: List[Employee]):
        for employee in employees:
            if employee.available:
                await employee.process_call(call)

if __name__ == '__main__':
    operators, supervisors, directors = 3, 2, 1
    cc = CallCenter(operators, supervisors, directors)

    t0 = datetime.datetime.now()

    async def main():
        calls = asyncio.Queue()
        await calls.put(Call("John", Severity.LOW))
        await calls.put(Call("Jane", Severity.MEDIUM))
        await calls.put(Call("Jack", Severity.HIGH))

        for _ in range(operators + supervisors + directors):
            asyncio.create_task(cc.dispatch(calls))        

        await calls.join()

    asyncio.run(main())
    print(f"total time to resolve all calls: {(datetime.datetime.now() - t0).total_seconds()}")