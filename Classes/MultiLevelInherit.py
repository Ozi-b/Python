# Too much of a good thing, is a bad thing!
# Too much inheritance between classes can increase complexity and introduce various kinds of issues
# Example: the penguin class inherits all the features of the bird class, BUT PENGUINS CAN NOT FLY!
# so I can create a penguin object and call the fly method on it even though penguins can not fly
# this is called inheritance abuse
# Another example is the concept of employees
# Employee is a person, and a person is a living creature, which is a thing..... you get the picture
# this can significantly increase the complexity of your software

# if you want to use inheritance limit it to 1 or 2 levels

class Animal:
    def eat(self):
        print("eat")


class Bird(Animal):
    def fly(self):
        print("fly")


class Penguin(Bird):
    pass
