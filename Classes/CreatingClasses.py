# Use Pascal naming for classes
# Normal naming: my_point
# Pascal naming: MyPoint

class Point:
    def draw(self):
        print("draw")


point = Point()
# you will see after the dot that not only the draw method is available but many others
# this is through "inheritence" which it got from another object in python
# point.draw (the method you created). point.__class__ (a method from another object in python inherited to ours)

# Returns <class '__main__.Point'>
# the main you see above is the name our module
print(type(point))

# isinstance will show if this object is an instance of a given class
# Returns True
print(isinstance(point, Point))

# Returns flase because point is not an instance of the int class
print(isinstance(point, int))
