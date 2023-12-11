items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

filtered = list(filter(lambda item: item[1] >= 10, items))
# passes a function through each tuple checking if the price is greater than or equal to 10 from the items list and will then filter it
print(filtered)
