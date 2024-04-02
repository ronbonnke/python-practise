
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




# EXAMPLES IN DETAIL

# LOCAL  VARIABLES ARE DECLARED WITHIN THE FUNCTION AND CAN ONLY BE USED INSIDE THAT FUNCTION.
# # only local works in this example :-


# GLOBAL LEVEL
# name = 'THIS IS A GLOBAL STRING'
def greet():
    # ENCLOSING LEVEL
    # name = 'Sammy'
    def hello():
        # LOCAL LEVEL
        name = "I'M A LOCAL"
        print('Hello ' + name)
    hello()
greet ()



# ENCLOSING VARIABLES ARE DECLARED OUTSIDE OF THE FUNCTION BUT CREATED WITHIN IT.
# only enclosing works in this example :-

# GLOBAL LEVEL
# name = 'THIS IS A GLOBAL STRING'
def greet():
    # ENCLOSING LEVEL
    name = "SAMMY & I'M ENCLOSING VARIABLE"
    def hello():
        # LOCAL LEVEL
        # name = "I'M A LOCAL"
        print('Hello ' + name)
    hello()
greet ()



# GLOBAL VARIABLES ARE DECLARED OUTSIDE OF ALL FUNCTIONS AND CAN BE USED BY ANY FUNCTION.
# only global works in this example :-


# GLOBAL LEVEL
name = 'THIS IS A GLOBAL STRING'
def greet():
    # ENCLOSING LEVEL
    # name = 'Sammy'
    def hello():
        # LOCAL LEVEL
        # name = "I'M A LOCAL"
        print('Hello ' + name)
    hello()
greet ()



#  BUILT-IN VARIABLES ARE PART OF Python language itself and can be accessed from anywhere in the script.













# new eg's:
x = 50
def func(x):
    print(f'X is a {x}')

    # LOCALLY RE-ASSIGNMENT
    x = 200
    print(f'I changed X locally to {x}')
func(x)



# eg's
x = 50
def func():
    global x
    print(f'X is a {x}')

    # LOCALLY RE-ASSIGNMENT ON GLOBAL VARIABLE
    x = "NEW VALUE"
    print(f'I locally changed GLOBAL X to {x}')
print(x)
func()
print(x)

# or use this way
x = 50
def func(x):
    print(f'X is a {x}')

    # LOCALLY RE-ASSIGNMENT ON GLOBAL VARIABLE
    x = "NEW VALUE"
    print(f'I locally changed GLOBAL X to {x}')
    return x
func(69)
print(x)
