# Primitive types can be numbers, booleans and strings

# variable
# value of this variable is a whole number also referred as an integer in programming
import math
students_count = 1000
rating = 4.99  # value of this variable is number that has a decimal point known as a float in programming
is_published = False  # value of this variable is a boolean which is either true or false
# Note: Python is case sensitive, meaning that uppercase and lowercase values will have different meanings. Boolean values should always start with an uppercase letter (True/False)
course_name = "Python Programming"  # value of this variable is a string
print(students_count)  # should log the number 1000

# variable names. 4 things to consider
# 1) Keep all variable names descriptive and meaningful.
student_grade = 92  # easy to understand as to what the value of 92 represents.
g = 92  # confusing as to what the value of 92 represents.
# 2) Use lower case letters to name your variables.
# 3) Use under score to seperate multiple words. This makes your code more readable because having a space between multiple words will cause errors.
# 4) Put a space before and after the equal sign(=). This makes your code more readable.

# Strings
# Strings are values that are words or sentences and need to be wrapped with single qoutes('') or double qoutes("")
course = "Python with Mosh"
# tripple qoutes are used to format a long string
message = """
Hi person!

  I like turtles :)

Good day

-turtle boy
"""
# the len function is used to get the length of a string
print(len(course))  # should log 16
# To get the individual character of a string use the square bracket and the number of the character that you are trying to return
# Note: strings are zero indexed meaning that the first character of the string is 0 not 1
print(course[0])  # should log the character P
print(course[5])  # should log the cahracter n
# To find a character in reverse order use the minus character. -1 will show the character at the very end of the string.
print(course[-1])  # should log the character h
print(course[-3])  # should log the character o
# sting slice
print(course[0:3])  # should log Pyt
# since there is no number at the end it will just copy the rest of the string, logging Python with Mosh
print(course[0:])
# if no number is added to the front, python will default to the zero index logging Pyt
print(course[:3])
print(course[:])  # this will create a copy of the original string


# Escape Sequences
# The backslash(\) character is known as a escape character and backslash double qoute("") is an escape sequence
# \"
# \'
# \\
# \n (short for new line)
escape_example = "Python \"Programming"
escape_line = "Python \nNew line"
print(escape_example)
print(escape_line)

# Formatted strings
first = "Brian"
last = "Ortiz"
# full = first + " " + last
# formatted string. You can also call other methods inside the curly braces and it will run during run time
full = f"{first} {last}"
full2 = f"{len(first)} {2 + 3}"
print(full)  # should log "Brian Ortiz"
print(full2)

# String Methods
string = "Hello World"
len(string)  # Shows the length of a string
string.upper()  # converts a string to uppercase
string.lower()  # converts a string to lowercase
string.title()  # converts the first letter of every word to uppercase
string.strip()  # removes white spaces in the string. lstrip removes the white spaces at the beginning of the string and rstrip removes the white spaces at the end of the string
# shows the index of a character. Note: python is case sensitive so be aware
string.find("Wor")
# Replaces what ever character you have as the first argument with whatever you have as the second argument
string.replace("H", "J")
# looks for the string you have written already in a seperate string. returns a boolean value
print("ello" in string)
# checks to see if the string you have written is NOT in a seperate string. returns a boolean value
print("swift" not in string)

# Number methods
# there are 3 different types of numbers
num = 1  # integers
num2 = 2.5  # floats
num3 = 1 + 2j  # complex numbers (a + bi)
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)  # returns a float
print(10 // 3)  # returns an integer/whole number
print(10 % 3)  # returns the remainder (modulus)
print(10 ** 3)  # exponent left to the power of right
# augmented assignment operator - can be used with any of these operators
x = 10
x += 3

# Working With Numbers
round(2.9)  # rounds up a float
abs(-2.9)  # returns the absolute value of a number
# look python 3 math module to learn more about math methods
print(math.ceil(2.2))

# Type Conversion
b = input("b: ")

r = int(x) + 1
print(f"b: {b}, r: {r}")
# int(x)
# float(x)
# bool(x)
# str(x)

# Falsy
# ""
# 0
# None
