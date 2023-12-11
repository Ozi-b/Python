# Class Attributes: The same across all instances of the class
# Example: a class attribute is like saying all humans have two eyes (class attribute) but they have different eye color (object attribute)

class Point:
    default_color = "red"  # class attribute

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
# Returns red: This is using the object reference to the class atribute
print(point.default_color)
# Returns red: This is referencing the class it self to return its class atribute
print(Point.default_color)

# You can change the class attribute outside of the class construction

Point.default_color = "Yellow"
print(point.default_color)  # Returns yellow
print(Point.default_color)  # Returns yellow
point.draw()
# Objects in python are dynamic so you dont have to define all the attributes in a constructor
# x & z are instance attributes
# Instance Attributes: belong to the point instances or point object meaning every point object can have different values for these attributes
# the another object is completely independent from the point object
another = Point(3, 4)
print(another.default_color)  # Returns yellow
# Note that even though another is a seperate object its collor also changed becuase its from the same class and has the same class attribute as point
another.draw()

# In practical terms you will be using instance attributes most of the time
# But there are times that you will want to use a class level attribute that is shared across all objects of a given type
