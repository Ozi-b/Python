#

from pathlib import Path

path = Path("Modules/ecommerce")
# path.exists()  # returns a boolean
# path.mkdir()  # creates a directory
# path.rmdir()  # removes a directory
# path.rename("ecommerce2")  # renames a directory

# with this we can get the list of files and directories in this path
# print(path.iterdir())
# returns <generator object Path.iterdir at 0x102923920>
# a generator object returns a new value everytime we iterate
# so when working with a large list of items and storing those items into memory, we use a generator object
# we iterate it and get a new value everytime, this is more efficient
# this is because you may work with directories that have a ton of files in it

# returns both the files and directories

# Modules/ecommerce/shopping
# Modules/ecommerce/__init__.py
# Modules/ecommerce/__pycache__
# Modules/ecommerce/customer

# for p in path.iterdir():
#     print(p)

# now for directories that DONT have a ton of files in it
# you can convert this generator into a list by using a list comprehension

paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)
# this will give you an array of posix path objects
# [PosixPath('Modules/ecommerce/shopping'), PosixPath('Modules/ecommerce/__init__.py'), PosixPath('Modules/ecommerce/__pycache__'), PosixPath('Modules/ecommerce/customer')]
# whats PosixPath?
# The path import above is the base path for two classes. PossixPath and windows
# PosixPath is used for mac and linux systems

# the if statement in line 32 will now show case the directories in this path
# [PosixPath('Modules/ecommerce/shopping'), PosixPath('Modules/ecommerce/__pycache__'), PosixPath('Modules/ecommerce/customer')]

# know that itdir() is useful to get the list of files and directories in a path but it has two limitations
# 1) we cannot search by a pattern
# 2) does not search recursively

# this is where glob come in
py_files = [p for p in path.glob("*.py")]
print("All py files: ", py_files)
# returns [PosixPath('Modules/ecommerce/__init__.py')]

# To search recursively insert **/*.py in the argument for glob on line 48
# you can also search recursively by using rglob (path.rglob())
# this will show all the py files and its children
