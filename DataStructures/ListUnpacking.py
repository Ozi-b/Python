numbers = [1, 2, 3, 4, 5]
first, second, *other = numbers
# with this syntax you will store first and second items while the rest will be stored into other
print(first)  # prints the number 1
# prints numbers 3, 4 and 5 (notice how it did not print the number from the list)
print(other)

first, *other, last = numbers
print(first, last)
print(other)
