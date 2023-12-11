letters = ["a", "b", "c"]
items = (0, "a")
index, letter = items
print(index)
print(letter)
for index, letter in enumerate(letters):
    print(index, letter)

# enumerate will showcase the index of each item (0,"a") (1, "b") (2, "c") known as a tuple
# lists are wrapped with braces while tuples are wrapped with parentheses
