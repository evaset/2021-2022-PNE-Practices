class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles."

car1 = Car("blue", 20000)
car2 = Car("red", 30000)
print(car1)
print(car2)

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    def speak(self, sound):
        return f"{self.name} says {sound}"
class GR(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)
dog = Dog("Lucas", 4,)

dog = GR("Lucas", 4)
print(dog.speak())
print(dog)

