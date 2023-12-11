# F2 is used to rename objects in vscode

class TagCloud:
    def __init__(self):
        # high light tags and hit F2 and prefix tags with 2 underlines (__tags)
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud.add("python")
cloud.add("python")
cloud.add("python")
# This will cause an error because there is no key of PYTHON because it is all stored in lowercase
# This is because this class gives underlying access to the underlying dictionary that is used to keep
# track of the count of text
# We need to hide this attribute from the outside
# print(cloud.__tags["PYTHON"])


# After making the changes you no longer have .tags and .__tags produces an error
# AttributeError: 'TagCloud' object has no attribute '__tags'
# in a way its telling the consumer "Hey dont touch this! It's private!"
# mainly used to avoid accidental access to these members
# print(cloud.__tags)

# To access it you need to use __dict__
print(cloud.__dict__)  # Returns {'_TagCloud__tags': {'python': 3}}
# print(cloud._TagCloud__tags)  # Returns {'python': 3}
