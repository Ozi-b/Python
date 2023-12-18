# We dont write all of our code in one file spanning thousands of lines of code
# We should split our code into multiple files
# A module is a file that contains some python code
# A module should contain highly related objects like objects, classes, variables and so on

# For example these two functions are highly related to the concept of sales

# lines 10-11 and 14-15 have been moved to the sales file

# def calc_tax():
#     pass


# def calc_shipping():
#     pass

# we have now imported the two functions from the sales file into this file

from ecommerce.shopping.sales import calc_shipping, calc_tax

calc_shipping()
calc_tax()

# you will come to find that a lot of coders use the asterisk to pull all funcitons from one file
# this is bad practice because if you blindly import all the functions or variables
# it can overwrite your objects with the same name in your current file causing bugs

# from sales import *

# Another way is to transfer functions is to just use import
# now we can use calc_shipping and calc_tax as an object method
# making the sales file an entire object
# import sales

# sales.calc_shipping()
