numbers = [3, 51, 2, 8, 6]
numbers.sort()
print(numbers)
# .sort will sort out the list in accesending order

numbers.sort(reverse=True)
print(numbers)
# sorts in reverse order

nums = [32, 70, 43, 29, 69]
# will print a new list that is sorted and will not modify the original list
print(sorted(nums))
print(sorted(nums, reverse=True))
print(nums)

items = [
    ("Product1", 10),
    ("Product2", 5),
    ("Product3", 19),
    ("Product4", 15)
]

print(items)


def sort_item(item):
    return item[1]


# print(sort_item(items))

items.sort(key=sort_item)
print(items)
