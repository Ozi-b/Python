x = 10
y = 11

z = x
x = y
y = z

print("x", x)
print("y", y)
# this process is rather confusing and there is a better way to swap the values of variables

a = 15
b = 30

a, b = b, a
print("a", a)
print("b", b)

# on line 15 the right side of the assignment operator we are defining a tuple
# remember that tuples are defined with paranthesis but does not need them to create them
# line 15 can be translated to this a, b = (30, 15)
# we are using unpacking a which is assigned to 30 and b which is assigned to 15
