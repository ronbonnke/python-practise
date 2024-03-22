# learn to print the statements and move on to the next step
print("hello world")
print('Welcome to python : The world of real snakes')

print("3+6 : " , 3 + 6)

 # division is not equal to integer division. It gives a decimal value
print("3/6 : ", 3 / 6) 

print("3*6 : ", 3 * 6)
print("3-6 : ", 3 - 6)
print("3%6 : ", 3 % 6)

# checking condition
print("3!=6 : ", 3 != 6)

print("3&6 : ", 3 & 6)

# checking condition
print("3==6 : ", 3 == 6)

# use power 
# code explanation  2*2*2 = 8
print("2 ** 3 : ", 2 ** 3)


# you can find out which operator gets the first preference while calculating these (basic Arithmetic operations)

print("2+10*10+3 : ", 2+10*10+3)

print("(2+10)*(10+3) : ", (2+10)*(10+3))

print("2+(10*10)+3 : ", 2+(10*10)+3)

print("(2+10)*10+3 : ", (2+10)*10+3)

print("2+10*(10+3) : ", 2+10*(10+3))


# eg1
a = 10
a = a+a
print(a+a)
print(type(a))

# eg2
a = 30.1
print(a)
print(type(a))

# eg3
my_income = 100
tax_rate = 0.1
my_taxes = my_income * tax_rate
print(my_taxes)


print('hello')
print("hello")
print("I'm Ron")



myString = "abcdefghijk"
print(myString[2])

# we use colon to print the rest other numbers starting from the index number 2 which is c.
#  but here the starting point of the index is included here including the index 
myString = "abcdefghijk"
print(myString[2:])

#here it goes upto the index 4 but it doesn't include the 4th index keep that in mind
myString = "abcdefghijk"
print(myString[:4])


# you can see it goes till the required index in right but gives the previous value
print(myString[3:6])
print(myString[2:4])

# lets print all the string "abcdefghijk"
print(myString[0:11])

# there's one more way to print all strings
print(myString[::])

# for skipping numbers
print(myString[::2])

# for skipping from a particular index
print(myString[2:7:2]) 


# --- just a trick ---- #
# for REVERSING the given string
print(myString[::-1])

# add
print(2+3)

# concat
print('2' + '3')

x = "Hello World"
print(x.upper())
print(x.lower())

print(x.split())

# more eg's for split method()
x =  "I love Python programming"
print(x.split())



# try concat(+) again
name = "Ron"
print("My name is",name)
print("My name is "+ name)

# formatting
# use single quotes 
print('This is a string {}'.format('INSERTED'))




# The number inside the braces are index values
print('There are {1}, {0}, {2} in the jungle'.format('fox','lion','tiger'))

print('There are {1}, {1}, {1} in the jungle'.format('fox','lion','tiger'))

print('There are {1}, {2}, {0} in the jungle'.format('fox','lion','tiger'))




# eg using literals  or
#  . dot format method 
print('There are {f}, {t}, {l} in the jungle'.format(f='fox',l='lion',t='tiger'))

print('There are {f}, {f}, {f} in the jungle'.format(f='fox',l='lion',t='tiger'))


# float formatting
result = 100/777
print(result)
print("The result was {}".format(result))
# or
print("The result was {r}".format(r=result))


#floatFormatting "{value:width.precision f}"
print("The result was {r:1.3f}".format(r=result))

# width inside it (creates a white space)
print("The result was {r:10.5f}".format(r=result))

# passing the formatting through the f letter inside {}   here we are using literals 
name = "Ron"
print(f"Hello, My name is {name}")

# eg1 
name = "Ron"
age = 21
print(f"{name} is {age} years old.")



# LIST

my_list = [1,2,3]
my_list = ['string', 200, 50.46]
print(len(my_list))
print(my_list[1:])


another_list = ['box',5]
new_list = my_list + another_list
print(new_list)
new_list[0] = 'Bonnke'
print(new_list)
new_list[4] = 'lcar'
print(new_list)


# append helps you to add a element in the end of the list
new_list.append(25)
print(new_list)

new_list.append("hey yoo")
print(new_list)




#  pop is used to remove the last element from the list

# pops the element and doesn't return
new_list.pop()
print(new_list)
# returns the popped element
print(new_list.pop())
print(new_list)



new_list = ['u', 'o', 'a', 'i', 'e']
num_list = [4,2,8,3]

new_list.sort()
print(new_list)


num_list.sort()
print(num_list)
# or
num_list.sort()
my_sorted_list = num_list
print(my_sorted_list)

num_list.reverse()
print(num_list)



# DICTIONARY

my_dict = {'key1':'value1','key2':'value2',}
my_dict['key1']
print(my_dict['key1'])

# example 1
price = {'apple':2.89,'banana':5}
print(price['apple'])

# example 2
d = {'k1':20,'k2':[0,1,2],'k3':{'insideKey':100}}

print(d['k1'])

print(d['k2'])


# here im  accessing inside key of k3 using its index
print(d['k2'][2])

print(d['k3'])

print(d['k3']['insideKey'])


# This is the example for  how to add new items in dictionary
list = ['a','b','c']
letter = list[0].upper()
print(letter)

# This is also example for  adding a new item into dictionary
d = {'k1':100, 'k2':200}
d['k3'] = 300
print(d)

# re assigning
d['k1']=720
d['k2']=456
d['k3']='HEY'
print(d)

# if you want the old dictionary value
d = {'k1': 100, 'k2': 200, 'k3': 300}
print(d)

# To return keys  from dictionary
print(d.keys())

#  To return values 
print(d.values())

#  This  will give both keys and values in parenthesis
print(d.items())


# you can check the   typeOf   here
tups = (1,2,3)
list = [1,2,3]
print(type(tups))
print(type(list))

# To count 
tups = ('a', 'b', 'c', 'a', 'a')
print(tups.count('a'))


#  List can replace and take place inside a list
list[0] = 'NEW'
print(list)

# ( Tuple cannot  be replaced or taken place inside tuple  /  IT DOESN'T NOT SUPPORT ITEM ASSIGNMENT

# tups[0] = 'z'
# print(tups)
# ///////////

#  SETS
mySet = set()
print(mySet)  #returns empty set



# add a set
mySet.add(8)
print(mySet)
# output may look like dictionaries but it's not be'cos they dont have key value pairs 😂😂



# you can continue adding your set but same numbers cannot be added

# set must have unique value's so we cannot add same numbers or repeat them
mySet.add(2)
mySet.add(9)
mySet.add(4)
print(mySet)

# keep in mind sets take only unique value
# use set() method
my_list = [1,1,1,2,2,6,4,4,6,2]
print(set(my_list))


# example from Udemy academy
Mississippi = ['M','i','s','s','i','s','s','i','p','p','i']
print(set('Mississippi'))


print(set((1,1,2,3)))

#  BOOLEANS

print(type(False))


# checking true or fale bool conditions
check = 1 > 2
print(check)

check = 1 == 1
print(check)

print((60+(10 ** 2) / 4 * 7) - 134.75)

4*(6+5)
4*6+5
4+6*5

# square root
100 ** 0.5

# reverse using slicing
s = 'hello'
print(s[::-1])


[0]*3     # print in terminal and check this



#  Comparisons [booleans]

1 == 2
1<2<3
1<2>3
1 == 2 and 20 != 10
12 >= 14 or 20 <= 25

# conditions with if else statements

if True:
    print("its true")

if 3>2:
    print("I'ts True")


# eg1
hungry = True
if hungry:
    print("feed me")




# eg2 using if
if hungry == True:
    print("feed me")
else:
    print("I'm not hungry")

# eg2 using if and else
hungry = False
if hungry:
    print("feed me")
else:
    print("I'm not hungry")


# eg3 using elif

loc = 'bank'
if loc == "super market":
    print("buy groceries")
elif loc == "bank":
    print("withdraw money")
else:
    print("stay home")



loc = 'super market'
if loc == "super market":
    print("buy groceries")
elif loc == "bank":
    print("withdraw money")
else:
    print("stay home")


loc = 'hill station'
if loc == "super market":
    print("buy groceries")
elif loc == "bank":
    print("withdraw money")
else:
    print("stay home")



#  eg 4

name = 'ron'
if name == 'sammy':
    print("small boy sammy")
elif name == 'franky':
    print("hello franky")
else :
    print("I don't know you")


#  Iterable
#  LOOPS
#  { in } is a keyword which gives the elements inside iterables.
numbers = [1,2,3]
for item in numbers:
    print(item)

# eg 1
myList = [1,2,3,4,5,6,7,8,9,10]
for elements in myList:
    print(elements)

# see the diff
myList = [1,2,3,4,5,6,7,8]
for element in myList:
    print("hello")



# eg2
# printing even nums
for element in myList:
    if element % 2 == 0:
        print(element)
    else:
        print("odds no. :",element)

# there's one more way
for element in myList:
    if element % 2 == 0:
        print(element)
    else:
        print(f'odd num: {element}')

# eg
# see print line 
myList = [1,2,3,4,5,6,7,8]
listSum = 0
for num in myList:
    listSum = listSum + num
print("sum of all ele: ",listSum)

# eg for IndentationError space
#  see print line
myList = [1,2,3,4,5,6,7,8]
listSum = 0
for num in myList:
    listSum = listSum + num
    print("sum of all ele: ",listSum)

# string printing
myString = "Hello World"
for letter in myString:
    print(letter)

# string printing
for letter in "Hello World":
    print(letter)

# to print anything we wish
for letter in "Python is fun":
    print("python")

tup = (67,12,33)
for item in tup:
    print(item)


# let's print the items inside tuples
myList = [(1,2),(3,4),(5,6),(7,8)]
print(len(myList))
for item in myList:
    print(item)


# new eg
for (a,b) in myList:
    print(a)
    print(b)

# new eg
for (a,b) in myList:
    print(a)


# new eg this print separate separately
for a,b in myList:
    print(a)
    print(b)