#

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


point = Point(10, 20)
another = Point(1, 2)

# Returns false because the == operator compares the reference or addresses of these two objects in memory
# But by having the def __eq__ magic method in the class it will now return true
print(point == another)

# print(point > other) returns an error stating > not supported between instances of point and point
# now with the def __gt__ magic method in the class it will return true or false if either point object is greater or less than
print(point > another)  # Returns true
print(point < another)  # Returns false
