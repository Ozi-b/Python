# The Animal class inherits from another class called object even though it was not added via paranthesis like we did with mammal and fish
# Object is the base class for all classes in python

class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
# Tells us if an object is an instance of a given class
print(isinstance(m, Mammal))  # Returns true

# Returns true because Mammal inherits from Animal
print(isinstance(m, Animal))
# Returns true because Animal inherits from Object
print(isinstance(m, object))

# Method for creating an empty object
o = object()
# Typing in o. will show all the magic methods for objects
# Typing in m. will also show all the magic methods inherited from object and the methods we have created in the class

# will show if an object is a child, sub class of another object class
print(issubclass(Mammal, Animal))
print(issubclass(Mammal, object))
