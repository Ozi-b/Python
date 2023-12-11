letters = ["a", "b", "c", "d", "e", "f"]
print(letters)

# Add to the end of the list
letters.append("g")
print(letters)
# Insert at a certain index
letters.insert(0, "-")
print(letters)

# Remove
letters.pop()  # should remove the letter g at the end of the list
print(letters)
letters.pop(0)  # should remove the item at the index of the list (removes "-")
print(letters)
letters.remove("b")  # removes the first occurence of the letter "b"
print(letters)
# removes a range of items. a single number refers to the index and the second refers to the end index
del letters[0:3]
print(letters)
letters.clear()  # removes all items from the list
print(letters)
