# To achieve polymorphic behaviour you start by defining a base class
# In this class we define the common behavior or method that we need in this derivative or children
# In this we achieve polymorphic behavior in line 22

# from abc import ABC, abstractmethod


# class UIControl(ABC):
#     @abstractmethod
#     def draw(self):
#         pass


# class TextBox(UIControl):
#     def draw(self):
#         print("TextBox")


# class DropDownList(UIControl):
#     def draw(self):
#         print("DropDownList")


# def draw(controls):
#     for control in controls:
#         control.draw()

# keep note that this draw will take a different form depending on the type of the control object

# -- But because python is a dynamically typed langauge, you dont need this UIControl base class
# we can still achieve the same outcome even thoug we have deleted the UIControl class


class TextBox:
    def draw(self):
        print("TextBox")


class DropDownList:
    def draw(self):
        print("DropDownList")

# Remember that the controls parameter is just a label/name
# As long as it is an iterable, python will be happy
# So its iterable parts should have a draw method
# python does not care if these come from the UIControl class
# As long as these parts have a draw method ofcourse
# Duck typing: if it walks like a duck, and quacks like a duck, then its a duck
# In other words python is only looking for the existence of certain methods in our objects


def draw(controls):
    for control in controls:
        control.draw()

# Although having a ui controlled base class as an abstract base class is a good practice
# Because it enforces a common interface or a common contract across all its derivatives
# With this we can make sure that every kind of ui control will have a draw method
