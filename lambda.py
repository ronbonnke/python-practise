def square(num):
    return num**2
my_nums = [1,2,3,4,5,6]
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



# filter function for even
def check_even(num):
    return num%2 == 0
mynums = [1,2,3,4,6,5,7,8,9,10]
print(list(filter(check_even, mynums)))


# printing squares in lambda
def square(num):
    return num**2
print(square(3))



# using lambda here
square = lambda num: num**2
print(square(6))

print(list(map(lambda num:num**2,my_nums)))

print(list(filter(lambda num:num%2 == 0,my_nums)))

print(names)
print(list(map(lambda name:name[0],names)))

# reverse
print(list(map(lambda x:x[::-1],names)))
