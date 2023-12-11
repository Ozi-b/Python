# Constructor: a special method that is called when we create a new point object
# To create a constructor, create a function with __init__
# __init__: a magic method is a constructor and is executed when we create a new point object.
# Remember that all methods in a class need at least one parameter called self
# Self: a reference to the current point object

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
# an object can also have attributes which are basically variables that include data about the object
# Example: humans have attributes like eye color, height, weight etc. And also have functions like walk and talk
# Returns 1
print(point.x)
point.draw()
