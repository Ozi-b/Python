# Dictionaries is an object that stores key value pairs
point = {"x": 1, "y": 2}

# the dict() function can be used to create dictionaries simmilar to creating list's by using the list() function
point = dict(x=1, y=2)

print(point["x"])

# you can change the value of a key
point["x"] = 10

# you can add a new key value pair to a dictionary
point["z"] = 20

print(point)

# invalid value and will produce an error
# print(point["a"])
# this version will not produce an error
if "a" in point:
    print(point["a"])

# this line has the same functionality as lines 20 and 21 and will return None
# the zero will be returned if a key of "a" is not found
print(point.get("a", 0))

# deletes a key
del point["x"]
print(point)

# will print the key's in the dictionary and its value
for key, value in point.items():
    print(key, value)
