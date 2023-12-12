# you can inhertance with built in types
# the following class is inheriting from the built in string class
# meaning that our class is inherting all the features from python strings
# and we can also add our own features to it


class Text(str):
    def duplicate(self):
        return self + self


text = Text("Python")
# as you can see, our class can also the lower() method that is used on string methods
# despite us building that method ourselves
print(text.lower())
print(text.duplicate())


class TrackableList(list):
    def append(self, obj):
        print("Append called")
        super().append(obj)


# list.append() adds an item to the end of a list
# but on the trackablelist class we have overidden the append method to include a print code that will print "Append Called"
test_list = TrackableList()
test_list.append("1")
