numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}

# will return all the items that are either in the first and second set
print(first | second)
# will return the only number that exists in both first and second which should be 1
print(first & second)
# will show the difference between the two sets which is 2, 3 and 4
print(first - second)
# will return the items that are either in first or second but not both
print(first ^ second)


# sets are unordered collections meaning they are not stored in sequence
# print(first[0]) # this will produce an error

if 1 in first:
    print("yes")
