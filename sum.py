def myfunc(a,b):
    return sum((a,b)) * 0.05
print(myfunc(60,40))



def myfunc(a,b,c=0,d=0):
    return sum((a,b,c,d)) * 0.05
print(myfunc(60,40,20,50))


# To add many arguments
# always use args but can use other words too but use only args while using (*) to add many args
def func(*args):
    return sum(args) * 0.05
print(func(10,20,100))


