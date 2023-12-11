# The with statement will automatically close a file whether we have a final clause or not
# file has methods that start with 2 underlines (__) these are known as magic methods
# you can use multiple file such as reading one file and writing to another
# with open("WithStatement.py", encoding="utf-8") as file, open(another_file.txt) as target:

try:
    with open("WithStatement.py", encoding="utf-8") as file:
        print("File opened.")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
