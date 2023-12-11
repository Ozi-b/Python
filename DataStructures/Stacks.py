# LIFO - Last In First Out

browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
# .append to add an item on top of the stack
print(browsing_session)

last = browsing_session.pop()
# .pop to remove item on top of the stack
print(last)
print(browsing_session)
if not browsing_session:
    print("disable")
# checks stack if its empty or not
print("redirect", browsing_session[-1])
# index -1 to get the item on top of the stack
