# currently all of our files are in the modules folder
# but as our application grows, you will want to organize these files into sub directories
# otherwise you will end up with hundreds or even thousands of python files into one folder which is not good
# So we are going to create a sub-directory called ecommerce and move the sales file to it

# After moving the sales file into the ecommerce folder you will see that the other files
# that were importing from sales.py now have a red underline because it cannot find the sales module
# to fix this issue, we will add a file into the ecommerce sub-directory called __init__.py

# --- Extra notes in the __init__.py file ---#

# after you make the changes go to any of the files that was importing from sales
# and update it with ecommerce.sales as well as its objects
# example: ecommerce.sales.calc_tax()

# A better way of doing it is using from

# by using from ecommerce.sales import calc_tax
# you can then just call the function by it self
# example: calc_tax()

# Now if the module containes a ton of methods and you dont want to add all the methods on the from line
# you can just use from ecommerce import sales
# and then call the function like an object method
# example: sales.calc_tax()
