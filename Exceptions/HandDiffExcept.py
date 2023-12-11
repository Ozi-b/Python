# Run this program in the bash terminal
# enter 0 as the age. It will produce a ZeroDivisionError
# This is becuase it is only handling value error exceptions

# try:
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except ValueError:
#     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were thrown.")

# Now that you have included a ZeroDivisionError exception, the program will return "You didn't enter a valid age." and continue running.
# Note that since the message is repeated you will have to change it in the future in two places
# but by having (ValueError, ZeroDivisionError) code, it will throw the proper exception if either or exception is thrown
# Also note that if one of the except clauses is executed all the other ones are ignored

try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
