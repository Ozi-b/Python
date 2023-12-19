# absolute import
# from ecommerce.customer import contact

# related import
# one dot (.) equals the current package
# two dots (..) equals one level up bringing you to the ecommerce package

# -- Executing Modules as Scripts -- #
# you can write statements in a module and these statements will be executed the first time that the module is loaded
# so if you import this module in a few different modules in our program,
# python will load this program only once and store it in cache memory
# so the statements written here will be executed once
# now press command + p (mac) / control + p (windows) and go to the CreatingModules.py file and run it
# you will see that the print("Sales initialized") line of code was executed
# using the same technique you can write the initialization code for our packages
# command + p again and go to the __init__.py file in the ecommerce pacakge
# create a print("Ecommerce initialized") code in that file
# go back to the CreatingModules.py file and run it
# you will see that it now prints Ecommerce initialized and Sales initialized

# lets take it to the next level and also print the name of the sales module in line 27
# with the __name__ added onto to the print line it will return Sales initialized ecommerce.shopping.sales when you run it in the CreatingModules.py file
# but if you run the sales module it will return Sales initialized __main__
# so the name of the module that starts our program is always main

from ecommerce.customer import contact

contact.contact_customer()


# print("Sales initialized", __name__)


def calc_tax():
    pass


def calc_shipping():
    pass


# -- Executing Modules as Scripts -- #
# this code we can make this file usable as a script as well as a usable module that we can import into another module
# now if this code is executed on another file it will not work because the name of the file will not be __main__
if __name__ == "__main__":
    print("Sales starte")
    calc_tax()
