def square(num):
    return num**2
my_nums = [1,2,3,4,5]
for item in map(square, my_nums):
    print(item)

my_var = list(map(square, my_nums))
print(my_var)





# this eg is for  the filter() function.  It filters out all even numbers from a list of integers and returns them as a new list.

def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]
names = ['Andrea','Molly','Dolly','bonnke']
print(list(map(splicer, names)))
