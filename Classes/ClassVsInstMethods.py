# There are instance methods as well as class methods
# def __init__ and def draw(self) are instance methods so we can call them using an instance of the point class using an object such as point.draw() in line 14

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod  # this is a decorator and its a way to extend the behavior of a method or function
    def zero(cls):  # cls stands for class which is a reference to the class it self. you can call it anything but by convention its best to use cls
        # exactly like calling Point(0, 0). the difference is that when you run the zero() method python will pass a reference to the point class zero method
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


# Returns Point (0, 0)
point = Point.zero()  # this method is defined at the class level and when you call it, it will initialize with the values of point(0, 0)
# the zero() method is a factory method becuase like a factory, it creates a new object
# initializing an object can be complex and mmight require that you add some magical values like point(0, 0, 1, "a")
# to avoid this, you can create a factory method that will return an object with the values needed moving the complexity to the factory method
point.draw()
