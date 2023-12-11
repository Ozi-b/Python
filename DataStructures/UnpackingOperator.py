
# this will print [1, 2, 3] but what if you want an output of 1 2 3?
numbers = [1, 2, 3]
print(numbers)

# to achieve the output of 1 2 3 you will need to use the unpacking operator (*)
# * will unpack a container, take out its individual elements and pass them as arbitrary arguments to print function
print(*numbers)

ListObject = list(range(5))
print(ListObject)
ListObject = [*range(5), *"Hello"]
print(ListObject)

first = [1, 2]
second = [3, 4]

# you can unpack and combine lists and other things
combine = [*first, "a", *second, *"Hello"]
print(combine)

firstDict = {"x": 1}
secondDict = {"x": 10, "y": 2}
combined = {**firstDict, **secondDict, "z": 1}
print(combined)  # notice how the x key value is now 10
