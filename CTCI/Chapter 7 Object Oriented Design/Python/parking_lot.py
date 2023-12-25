from dataclasses import dataclass
from abc import ABCMeta, abstractmethod
from typing import List

@dataclass
class Vehicle:
    number_plate: str
    owner_name: str
    owner_contact: str
    num_spots_required: int

class Motorcycle(Vehicle):
    def __init__(self, number_plate: str, owner_name: str, owner_contact: str, num_spots_required: int):
        super().__init__(number_plate, owner_name, owner_contact, num_spots_required)

class Car(Vehicle):
    def __init__(self, number_plate: str, owner_name: str, owner_contact: str, num_spots_required: int):
        super().__init__(number_plate, owner_name, owner_contact, num_spots_required)

class Bus(Vehicle):
    def __init__(self, number_plate: str, owner_name: str, owner_contact: str, num_spots_required: int):
        super().__init__(number_plate, owner_name, owner_contact, num_spots_required)

class ParkingSpot(metaclass=ABCMeta):
    def __init__(self):
        self.vehicle_type = ''
        self.owner_name = ''
        self.owner_contact = ''
        self.consecutive_parking_spots_taken = 0

    def is_available(self):
        return self.consecutive_parking_spots_taken == 0

    def assign(self, vehicle):
        self.vehicle_type = getinstance(vehicle)
        self.owner_name = vehicle.owner_name
        self.owner_contact = vehicle.owner_contact
        self.consecutive_parking_spots_taken = vehicle.num_spots_required

        print(f'Vechile {self.vehicle_type} belonging to {self.owner_name} has been parked.')

    @abstractmethod
    def can_accomodate(self):
        raise Exception('Method not implemented.')

class MotorcycleSpot(ParkingSpot):
    def can_accomodate(self, vehicle: Vehicle):
        return isinstance(vehicle, Motorcycle)

class CompactSpot(ParkingSpot):
    def can_accomodate(self, vehicle: Vehicle):
        return isinstance(vehicle, (Motorcycle, Car))

class LargeSpot(ParkingSpot):
    def can_accomodate(self, vehicle: Vehicle):
        return isinstance(vehicle, (Motorcycle, Car, Bus))

class Level:
    _parking_spots: List[ParkingSpot] = []

    def __init__(self, num_motorcycle_spots, num_compact_spots, num_large_spots):
        self._parking_spots += [MotorcycleSpot() for _ in range(num_motorcycle_spots)]
        self._parking_spots += [CompactSpot() for _ in range(num_compact_spots)]
        self._parking_spots += [LargeSpot() for _ in range(num_large_spots)]

        self._available_spots = num_motorcycle_spots + num_compact_spots + num_large_spots

    @property
    def available_spots(self):
        return self._available_spots

    @available_spots.setter
    def available_spots(self, val):
        self._available_spots = val

    def park(self, vehicle: Vehicle) -> bool:
        for i in range(len(self._parking_spots)):
            parking_spot = self._parking_spots[i]
            if not parking_spot.is_available():
                i += parking_spot.consecutive_parking_spots_taken

            consecutive_parking_spots = self._parking_spots[i : i + vehicle.num_spots_required]
            vehicle_can_fit = all(spot.is_available() and spot.can_accomodate(vehicle) for spot in consecutive_parking_spots)
            if vehicle_can_fit:
                parking_spot.assign(vehicle)
                return True
        return False

class ParkingLot:
    def __init__(self, levels, num_motorcycle_spots, num_compact_spots, num_large_spots):
        self._levels = [Level(num_motorcycle_spots, num_compact_spots, num_large_spots) for _ in range(levels)]

    def get_available_spot(self, vehicle: Vehicle):
        for level in self._levels:
            if level.available_spots >= vehicle.num_spots_required:
                parked = level.park(vehicle)
                if parked: return
        raise SpotUnavailableException

class SpotUnavailableException(Exception):
    pass