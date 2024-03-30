
#  LEGB rule is:
# Local , Enclosing, Global, Built-in.
# these  are in order of precedence and search for variables .
# if a variable is found then it stops searching further.
# LEGB is  used by python interpreter while executing any program.
# and also  tells us about scope of the variable.




# check the code block carefully to see which is inside which one

x = 25
def printer():
    x = 50
    return x
print(x)
print(printer())




# LOCAL  VARIABLES ARE DECLARED WITHIN THE FUNCTION AND CAN ONLY BE USED INSIDE THAT FUNCTION.







# ENCLOSING VARIABLES ARE DECLARED OUTSIDE OF THE FUNCTION BUT CREATED WITHIN IT.
# GLOBAL VARIABLES ARE DECLARED OUTSIDE OF ALL FUNCTIONS AND CAN BE USED BY ANY FUNCTION.
#  BUILT-IN VARIABLES ARE PART OF Python language itself and can be accessed from anywhere in the script.