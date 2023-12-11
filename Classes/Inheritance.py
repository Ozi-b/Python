# As you build classes you may find that you have classes that have features or functions that are in common
# For example all mammal's eat and walk
# But even though a fish will eat, it cannot walk they swim

# The issue with this is that you can see that that mammal and fish both share the eat method
# Even though its one line of code you will find that you may have the same method in different classes that have 5 or 10 plus lines of code
# This is bad because if there is a bug, you will have to fix it on multiple places
# Or if you want to change the behaviour, you will have to change the code in multiple places

# DRY: Don't Repeat Yourself!

# Inheritance allows us to define common behaviours in one class and then inheit them into another
# Now that the Animal class is created we can move the eat function into it
# and then include the eat function on both mammal and fish by including animal in paranthesis

# Animal is the parent, base class
# Mammal and fish is the child, sub class
class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    # def eat(self):
    #     print("eat")

    def walk(self):
        print("walk")


class Fish(Animal):
    # def eat(self):
    #     print("eat")

    def swim(self):
        print("swim")


# you can now see that the mammal class inherited the eat function from the parent animal class
m = Mammal()
m.eat()

# Inheritance is not limited to methods but can also inherit attributes of a base class
# in the class animal, a constructor has been set up with an age attribute set to 1
# now animal that has been constructed will have an age of 1
print(m.age)
