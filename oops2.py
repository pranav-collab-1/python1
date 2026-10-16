class Vehicle:
    def __init__(self,brand):
        self.brand = brand
class Car(Vehicle):
    def __init__(self, brand, fuel_type):
        super().__init__(brand)
        self.fuel_type = fuel_type
class ElectricCar(Car):
    def __init__(self, brand, battery_capacity):
        super().__init__(brand, "Electric")
        self.battery_capacity = battery_capacity
    def display(self):
        print(f"Brand: {self.brand}, Fuel Type: {self.fuel_type}, Battery Capacity: {self.battery_capacity} kWh")
car1 = ElectricCar("Tesla", 100)
car1.display()
