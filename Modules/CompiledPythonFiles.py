# When you run the CreatingModules.py file it will create a new folder called __pycache__
# In this folder we have the compiled version of the modules that we import into our program
# So we have the compiled version of the sales module
# The reason for this is to speed up module loading

# So the next time we run our program, python will look at this compiled folder
# If we do have the compiled version of the sales module, python will load that compiled version
# Skipping that compilation step resulting in faster loading of the sales module

# But how does it know that its getting the up to date version of this code?
# It basically checks the date and time of these two files (the compiled version and the source code)
# If the source code is newer then it realizes that it has changed so it will recompile it
