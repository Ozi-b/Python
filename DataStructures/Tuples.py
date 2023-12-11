# a tuple is a read only list
# you can use to contain a sequence of objects but you can not modify the list
# you define a tuple with paranthesis but you can also define it without paranthesis
point = 1, 2, 3
print(type(point))
# if you add only one item like removing the number 2 from point, python will only see it as a integer
# to fix this add a comma after the number one and python will then see it as a tuple
# you can define an empty tuple but having empty parathesis
concat = (1, 2) + (3, 4)
print(concat)
multiply = (1, 2) * 3
print(multiply)
# you can convert a list (or any iterable) to a tuple by using tuple()
convert = tuple([1, 2])
print(convert)
# like any iterable, you can find its index
print(convert[0])
print(point[0:2])
x, y, z = point
if 10 in point:
    print("exists")

# you can not modify a tuple so line 24 will not work
# point[0] = 10

# use tuple's for anything that you do not want to be modified
