# What if you want to add a constructor to mammal to label its weight
# Copy the init code in animal and paste it to Mammal and change age to weight
# This will produce an AttributeError: 'Mammal' object has no attribute 'age'
# The Attribute error occured because it initiliazed the constructor in mammal and ignored the animal constructor
# This is called method overriding

# By adding the super().__init__(), it will trigger the animal constructor first then the mammal constructor
# Running the program will give you this
# Animal Constructor
# Mammal Constructor
# 1
# 2

# so you can see that the Animal constructor was made first then the mammal constructor
# giving you the age of 1 and the weight of 2

# you can also change the order of these methods calls to where the animal constructor is called after we initialize the a mammal object
# to do this, move line 30 to the bottom of the __init__ method
# Mammal Constructor
# Animal Constructor
# 1
# 2
# as you can see the mammal constructor was initialized first, then the animal constructor
class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        # super().__init__() # this will give access to the base class of Animal and triggered the init method to establish the age of object
        print("Mammal Constructor")
        self.weight = 2
        super().__init__()

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
print(m.age)
print(m.weight)
