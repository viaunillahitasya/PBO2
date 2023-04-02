from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class pedicab(Vehicle):
    def start(self):
        print("Starting pedicab...")

class bicycle(Vehicle):
    def start(self):
        print("Starting bicycle...")

class electrickmotor(Vehicle):
    def start(self):
        print("Starting electrickmotor...")

vehicles = [pedicab(), bicycle(), electrickmotor()]

for vehicle in vehicles:
    vehicle.start()