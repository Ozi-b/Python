# generator objects are more efficient when working with extremely large sets of data. Generators are also iterable
# by chaning the brackets to paranthesis, the variable values no longer is a list but now a generator object

from sys import getsizeof
# getsizeof shows the amount of memory is used to store the data
# 1000 shows 200 bytes of memory and changing it to 100,000 will still show 200

values = (x * 2 for x in range(1000))
print("gen:", getsizeof(values))

# be aware that sense you can not store all the data in memmory, you wont be able to get the total number of items you are working with
print(len(values))

# changing the values variable to list and running getsizeof(values) will show a memory usage of 8856 bytes
values = [x * 2 for x in range(1000)]
print("list:", getsizeof(values))

# Use generator objects when using extremely large data sets or infinite data sets
