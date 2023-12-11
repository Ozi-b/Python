# Run this program in the bash terminal
# Now when you enter an invalid input (anything that is not a number),
# it will return "You didn't enter a valid age." and "Execution continues"
# Despite there being an incorrect input, by exceptions the program will continue to run instead of crashing

try:
    age = int(input("Age: "))
except ValueError as ex:
    print("You didn't enter a valid age.")
    print(ex)
    print(type(ex))
else:
    print("No exceptions were thrown.")
print("Execution continues.")
