items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

# prices = list(map(lambda item: item[1], items))

prices = [item[1] for item in items]  # does the exact same thing as line 7

# filtered = list(filter(lambda item: item[1] >= 10, items))

# does the exact same thing as line 11
filtered = [item for item in items if item[1] >= 10]
