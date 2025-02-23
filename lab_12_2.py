class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        return f"Brand: {self.brand}, Year: {self.year}"

class Car(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, year)
        self.model = model

    def display_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"

car = Car("Tesla", "Model S", 2023)
print(car.display_info())
