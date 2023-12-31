# Polymorphism: Many Forms
# our draw method is taking many different forms

from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


# def draw(control):
#     control.draw()

def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
# print(isinstance(ddl, UIControl))
# draw(ddl)

textbox = TextBox()
# draw(textbox)

draw([ddl, textbox])
