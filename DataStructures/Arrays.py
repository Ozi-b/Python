# arrays are a lot more effecient than lists when dealing with large sequence of numbers
# arrays take less memory and perform a little bit faster
# you will only see a difference with a sequence of numbers of 10k or more
# 90% of the cases you will use lists

# to use array's you will have to import it
from array import array
# look python typecode to see what what objects can be put in your array
numbers = array("i", [1, 2, 3])

numbers.append(4)  # appends a number to the end of a list
numbers.insert(2, 5)  # insert a number at a specific index
numbers.pop(2)
numbers.remove(1)
print(numbers)
# this will not work because 1.0 is a float and the "i" in array is for type integer
# err = numbers[0] = 1.0
print(numbers[0])
