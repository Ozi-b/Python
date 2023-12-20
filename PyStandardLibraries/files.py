#

from pathlib import Path
from time import ctime
# import shutil
path = Path("Modules/ecommerce/__init__.py")

# path.exists()
# path.rename("init.txt")
# path.unlink() # deletes a file

print(path.stat())  # returns info about this file
# os.stat_result(st_mode=33188, st_ino=26483799, st_dev=16777234, st_nlink=1, st_uid=501, st_gid=20, st_size=299, st_atime=1703019046, st_mtime=1703017732, st_ctime=1703017735)

# st_size: the size of the file in bytes
# st_atime: last access time
# st_mtime: last modify time
# st_ctime: the time the file was created

# the time value are seconds after epic which is the start of time of a computer
# this time is platform dependent
# in unix, the epic time is January 1st, 1970
# so to print the human readable time you will have to import ctime from the time module (line 4)

print(ctime(path.stat().st_ctime))
# returns Tue Dec 19 15:28:55 2023

# returns the content of the file as a bytesobject when representing binary data
path.read_bytes()

# returns the content of the file as a string
# print(path.read_text())
# using this method is easier then using the open() method
# with the open function you will have to specify multiple things as seen below

# with open("__init__.py", "r") as file:
#   ...

# but with read_text() it does all this already for you

# similar to read you can also write text onto a file
# both these methods take care of opening and closing a file
# path.write_text("...")
# path.write_bytes()

# There are all kinds of operations that we can do on a file using this path file
# However when it comes to copying a file this path object is not the ideal way to copy a file

# lets say i want to copy this file to a different location

# source is the current file
# source = Path("Modules/ecommerce/__init__.py")
# target path is the current directory plus the init file
# target = Path() / "__init__.py"

# first we need to read the content of the source (read_text())
# then we need to write it to the target (write_text())
# target.write_text(source.read_text())

# there is a better way by using shutil
# this module provides a number of high level operations for copying and moving files and directories
# now with shutil imported, we can copy files to the target like so
# shutil.copy(source, target)
