# A class can have multiple base classes
# The Manager class has the base class for Employee and Person
# This is known as Multiple inheritance and similarly to Multi level inheritance, it can be a source of issues

class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")


class Manager(Employee, Person):
    pass


manager = Manager()
# There are two greet methods that manager inherited and calling one of the greet methods
# When the greet method is called it will only call the first method from the object that is passed in first
# The interpreter will first look at the manager class to see if there is a greet method
# The manager class doesnt so the interpreter will then look at the parent classes for a grett method
# It will first find the employee greet method, run it and then terminate not even going to the person greet method
# This is bad because if someone changes the order of the greet method (Person, Employee) the structure of the code will completely change
# Only inherit classes when they have nothing in common
# It becomes problematic when classes have things in common like the greet method above
manager.greet()

# here is a good example of mulitple inheritance


class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FlyingFish(Flyer, Swimmer):
    pass
