letters = ["a", "b", "c", "d"]
letters[0] = "A"
print(letters)
print(letters[-1])  # prints the last item of the list
# you can use to indexes to slice a string. the same can be used to slice a list
print(letters[0:3])
# if you dont specify the first index, zero will be assumed by default
print(letters[:3])
# if you dont specify the second index, it will assume to fill to the end of the list
print(letters[1:])
print(letters[:])  # this will generate a copy of the original list
# when slicing a string, you can add a step ([::2] :2 is the step). this will negate every second element in the list
print(letters[::2])

numbers = list(range(20))
print(numbers[::2])
print(numbers[::-1])
# returns every item in the original list but in reverse order
