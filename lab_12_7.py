class Engine:
    def start_engine(self):
        return "Engine started"

class Wheels:
    def has_wheels(self):
        return "Has 4 wheels"

class Car(Engine, Wheels):
    def drive(self):
        return "Car is moving"

car = Car()
print(car.start_engine())
print(car.has_wheels())
print(car.drive())         
