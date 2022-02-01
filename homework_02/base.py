from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    started = False
    weight = 0
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started is False:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError()

    def move(self, distance):
        if (self.fuel - self.fuel_consumption * distance) < 0:
            raise NotEnoughFuel()
        else:
            self.fuel = self.fuel - self.fuel_consumption * distance
