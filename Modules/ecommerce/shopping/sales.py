# absolute import
# from ecommerce.customer import contact

# related import
# one dot (.) equals the current package
# two dots (..) equals one level up bringing you to the ecommerce package
from ..customer import contact

contact.contact_customer()


def calc_tax():
    pass


def calc_shipping():
    pass
