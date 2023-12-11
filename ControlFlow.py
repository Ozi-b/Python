# Comparison Operators
10 > 3  # greater than (true)
10 < 3  # less than (false)
10 >= 3  # greater than or equal to (true)
10 <= 3  # less than or equal to (false)
10 == 10  # equality (true)
10 == "10"  # equality (false because a number is not equal to a string)
10 != "10"  # NOT equal (true because a number is not a string)
"bag" > "apple"  # true because bag comes after so its considered greater
"bag" == "BAG"  # false because of the order of the characters
print(ord("b"))  # order number is 98
print(ord("B"))  # order number is 66
print("b" > "B")  # true becuase 98 is greater than 66

# Conditional Statements
temperature = 85  # Change the number to see the conditional at work
if temperature > 75:  # end the conditional with a colon
    print("It's warm")
    print("Drink water")
elif temperature > 65:  # elif is short for else if
    print("It's nice")
else:
    print("It's Cold")
print("Done")

# Ternary Operator
age = 12
# if age >= 18:
#     message = "Eligible"
# else:
#     message = "Not eligible"
# print(message)

# Line 35 is the same as lines 28-32. Line 35 is a ternary operator
message = "Eligible" if age >= 18 else "Not eligible"
print(message)

# Logical Operators
# and: specifies that if both conditions are true then the result is true
# or: if either or is true then the result is true
# not: inverses the value of a boolean
high_income = False
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("Eligible")


# // Short-circuit Evaluation //
# short-circuiting is where the code stops once it finds a true value. It first notices that the high_income is false and because of the or operator it moves on to the next argument
# which is good_credit (true) and stops there prints the result "eligible"
# with the and operator it will stop as soon it reaches a false value

# // Chaining Comparison Operators //
# age should be between 18 and 65 (age variable is in line 27)
age = 22
# if age >= 18 and age < 65:
if 18 <= age < 65:  # this line is the same as line 58
    print("Eligible")

# // For Loops //
for number in range(1, 10, 2):
    print("Attempt", number, number * ".")

# // For..Else //
successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

# // Nested Loops //
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

# // Iterables //
print(type(range(5)))  # returns object of range. Range is a complex types
# range is iterable
# strings are also iterable
for x in "Brian":
    print(x)

# lists store a list of objects (think of arrays in JS). Use square brackets to create a list([])
for x in [1, 2, 3, 4,]:
    print(x)

# // While Loops //
# While loops repeat something as long as a conditional is true
number = 100
while number > 0:
    print(number)
    number //= 2

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

# Infinite Loops
# Infinite loops run forever!

# while True:
#   command = input(">")
#   print("ECHO", command)
#   if command.lower() == "quit":
#     break
# always have a way to break an infinite loop or it will brick your computer (break statement in line 111)

# // EXERCISE //

count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")
