
#     **KWARGS   KeyWordARGS
def func(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I dont have a favorite fruit')
func(fruit='apple',veggie='lettuce')



# combination

def func(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[2],kwargs['fruit']))
func('10','to feed a','12',fruit='oranges',food='eggs',animal='cat')
