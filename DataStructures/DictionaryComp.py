# values = []
# for x in range(5):
#     values.append(x * 2)

# go through an iterable object(range(5)) pull the item (x) then do something with it (x * 2)
ListValue = [x * 2 for x in range(5)]  # list

SetValue = {x * 2 for x in range(5)}  # set

# dictionary. notice that you have to specify the key value pairs
DictValue = {x: x * 2 for x in range(5)}

print(ListValue)
print(SetValue)
print(DictValue)
