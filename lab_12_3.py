class Dog:
    def sound(self):
        return "Bark"

class Cat:
    def sound(self):
        return "Meow"

def animal_sound(animal):
    print(animal.sound())

dog = Dog()
cat = Cat()

animal_sound(dog)
animal_sound(cat)  
