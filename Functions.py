# // Defining Functions //


def greet():
    print("Hi there!")
    print("Welcome aboard!")


greet()
# after saving two line breaks will seperate the function from the rest of the code to make it look cleaner

# // Arguments //


def greet_person(first_name, last_name):  # parameters
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard!")


greet_person("Brian", "Ortiz")  # arguments

# // Types of Functions //


# 1) Perform a task
# 2) Return a value

def get_greeting(name):
    return f"Hi {name}!"


message = get_greeting("Brian")
print(message)
file = open("content.txt", "w")
file.write(message)


# // Keyword Arguments

def increment(number, by):
    return number + by


print(increment(2, by=1))


def increment2(number, by=1):
    return number + by


print(increment2(2))  # should print 3
print(increment2(2, 5))  # should print 7. Adding a different number on the second argument changes the by=1 parameter to then equal whatever you have added to as the second argument (by=5)
# by=1 is an optional parameter while number is a required parameter. optional parameter's should be added at the end/after the required parameter's
# increment(number, another, by=1) number and another parameter's are required while by=1 is optional

# // xargs


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))

# // xxargs


def save_user(**user):
    print(user)
    print(user["id"])


save_user(id=1, name="Brian", age=28)

# // Scope

result = "a"  # this is a global variable because now it can be found within the file
# it is best practice to use local variables since they do not allocate a lot of memory with in the file


def welcome(name):
    # global result # // global will pull the variable that you have named and change its value despite it being in local scope. THIS IS BAD PRACTICE! DO NOT DO THIS!!!
    result = "b"  # the scope of message is inside the greet function. This is known as a local variable or function scope


# this will not print due to the message variable not being within this scope
welcome("brian")
print(result)  # this will print "a" instead of "b" becuase the message variable in the welcome function is local scope not global scope


# // Debugging
# reference the multiply function in lines 59-63

print("Start")
print(multiply(1, 2, 3))
# indent the return total (line 63) to cause the bug
# when you run it, instead of getting Start 6, you will get Start 1

# // VScode Coding Tricks - Mac

# To instantly move your cursor to the beginning of a line or at the end of a line press function + left or right or up or down
print("Hello Brian!")

# To move a line up or down, hold down option (alt) and press up or down arrow key
# Turn lines of code into comments by holding down command and slash

# // Exercise! FIZZBUZZ
# if the input is divisible by three then it should return "fizz"
# if the input is divisible by five then it should return "buzz"
# if the input is divisible by both three and five then it should return "fizz buzz"
# if the input is not divisible by three or five then it should return the number it self


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz!"
    if input % 3 == 0:
        return "Fizz!"
    if input % 5 == 0:
        return "Buzz!"
    return input


print(fizz_buzz(5))
