# Lists, sets and dictionaries are container types
# you can also create your own containers
# the following code is an example of creating a container to contain the various tags in a blog

# This will also support the various operators around containers


class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()
cloud.add("python")
cloud.add("python")
# in a typical dictionary, this would return {'python': 2, 'Python': 1}
# we want to make our dictionaries smarter so that it will include both lower and upercase python key's
# to do this we will convert the tag to lowercase when the code is reading it in line 13
cloud.add("Python")
print(cloud.tags)  # Returns {'Python': 3} after the changes are made

# I want to be able to read the count of a tag like its done below
cloud["python"] = 10
len(cloud)
