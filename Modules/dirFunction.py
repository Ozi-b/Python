# wit the dir function you can get the list of attributes and methods defined in an object
# so in this object we are importing the sales module

from ecommerce.shopping import sales
# as you work in large projects, there are times that things dont work as you expect
# you can use the dir function for debugging

# when you run this program, you get an array of strings that contain all the attributes and methods in an object
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'calc_shipping', 'calc_tax', 'contact']
# print(dir(sales))

print(sales.__name__)  # returns the name of the module
print(sales.__package__)  # returns the name of the package
print(sales.__file__)  # returns the file name and address of the file
