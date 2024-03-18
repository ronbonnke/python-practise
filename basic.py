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

my_list = [1,2,3]
my_list = ['string', 200, 50.46]
print(len(my_list))
print(my_list[1:])

another_list = ['box',5]

new_list = my_list + another_list
print(new_list)

