# Magic methods are the methods that have two underscores at the beginning and the end of the method name
# they are called automatically by python interpreter depending on how we use our objects and classes
# Search up python3 magic methods to see the complete list
# https://rszalski.github.io/magicmethods/

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
print(point)  # Returns <__main__.Point object at 0x100c61c70> (comment out the def __str__ method in the class)
print(str(point))
# ---- __str__ ---- # The following is the default implementation of the __str__ magic method in the point object
# __main__ // name of the module
# .Point // class name
# 0x100c61c70 // the address of this point in memory
