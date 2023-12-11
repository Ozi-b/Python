# open() will open a file like a database file, network file and so on.
# it is important to close that file when you are done

try:
    file = open("CleaningUp.py", encoding="utf-8")
    age = int(input("Age: "))
    xfactor = 10 / age
    file.close()
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
finally:  # This will always run regardless if an exception is thrown
    file.close()
