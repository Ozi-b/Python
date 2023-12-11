#

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(10, 20)
another = Point(1, 2)
# Trying to add two points together will produce an error (TypeError: unsupported operand type(s) for +: 'Point' and 'Point')
# You can add two points together by implementing the __add__ magic method
# Now if you run it with the __add__ method above you will get <__main__.Point object at 0x1026e9d90>
# You get that result because the __str__ magic method is removed
# but if you store the result of this arithmetic operation into another object then it will add to objects together
combined = point + another
print(combined.x)  # Returns 11
print(combined.y)  # Returns 22
