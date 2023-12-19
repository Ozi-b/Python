# Paths are the foundation when working with files and directories

from pathlib import Path

# now you can create a path object in a few different ways

# absolute path (windows)
# Path("C:\\Program Files\\Microsoft")
# the double back slashes can be a little ugly
# you can simplify this by using a raw string
# in a raw string, back slash is not an escape character, it's taken literally as is
# Path(r"C:\Program Files\Microsoft")


# absolute path (mac/linux)
# Path("/user/local/bin")
# this represents the current folder
# Path()

# related path (mac/linux)
# Path("eccomerce/__init__.py")

# you can also combine path objects together
# path() / Path("ecommerce")
# or combine a path with a string
# path() / "ecommerce" / "__init__.py"

# you can get the home directory by using home
# Path.home() returns the home directory of the current user

path = Path("ecommerce/__init__.py")
# search up python 3 pathlib to find all the useful members for path

path.exists()  # returns whether this file or directory exists
path.is_file()  # returns whether it is a file or not
path.is_dir()  # returns whether it is a directory or not

# you can also extract individual components in this path which is extremely useful
print(path.name)  # returns __init__.py
print(path.stem)  # returns __init__
print(path.suffix)  # returns .py
print(path.parent)  # returns ecommerce
# you can use this to create a new path object based on this existing path but only change the name and the extension of the file
path = path.with_name("file.txt")
print(path)  # returns ecommerce/file.txt
# returns /Users/ozi-b/Documents/Coding/CodeWithMosh/Complete-Python-Mastery/Python/ecommerce/file.txt
# now this file does not exist yet, its only representing its path
print(path.absolute())
path = path.with_suffix(".txt")
print(path)  # returns ecommerce/file.txt
