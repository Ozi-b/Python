letters = ["a", "b", "c"]
print(letters.index("a"))
# if the item does not exist in the list, it will print an error stating ValueError: 'd' is not in list
if "d" in letters:
    print(letters.index("d"))

numbers = [1, 2, 3, 3, 4, 5, 5, 5]
print(numbers.count(5))  # will the number of times said item is in a list
