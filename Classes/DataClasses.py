# __eq__ this will allow us to compare the point objects and see if they are similar or not

from collections import namedtuple

# namedtuple will allow us to do the same thing as the point class but is much more readable and clean


Point = namedtuple("Point", ["x", "y"])


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y


# p1 = Point(1, 2)
# p2 = Point(1, 2)

p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
p1.x = 10

# Returns false because our point objects are in different locations in memory
# Because of the __eq__ method in the point class, it will now return true
print(p1 == p2)
# eventhough they share the same attributes
print(id(p1))  # Memory locations of p1
print(id(p2))  # Memory location of p2
