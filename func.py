

#  LEVEL 1

def lesserofeven(a,b):
    if a%2 == 0 and b%2 == 0:
        if a<b:
            result = a
        else:
            result = b
    else:
        if a > b:
            result = a
        else:
            result = b
    return result
print(lesserofeven(2,4))
print(lesserofeven(2,7))
print(lesserofeven(2,10))
print(lesserofeven(12,6))
print(lesserofeven(11,6))
print(lesserofeven(30,5))
# here above in printing statements its seeing odd even  numbers first then comparing them. But we need to  compare both the numbers at once.



# eg2

def lessEven(a,b):
    if a%2 == 0 and b%2==0:
        return min(a,b)
    else:
        return max(a,b)
print(lessEven(9,11))





# eg
def animal(word):
    wordlist = word.split()
    print(wordlist)

# the blow code checks the words after splitting the 0th and 1th index
    first = wordlist[0]
    second = wordlist[1]

    return first[0] == second[0] #checks  whether the first letter of both words is same or not
print(animal('level llama'))
print(animal('hover lama'))


# both are same codes only  difference is that in one function we have used 'if' condition and another has used 'else'
def animal(word):
    wordlist = word.split()
    return wordlist[0][0] == wordlist[1][0]
print(animal('level llama'))
print(animal('hover lama'))



# makes twenty
def makes_twenty(n1,n2):
    if(n1 == 20 or n2 == 20):
        return True
    elif(n1+n2 == 20):
        return True
    else:
        return False
print("checking =",makes_twenty(8,11))



 
# few examples for  functions
def old(name):
    first = name[0]
    inbetween = name[1:2]
    third = name[2]
    rest = name[3:]
    return first.upper() + inbetween + third.upper()  + rest
print(old('mcdonald'))


# same eg short code
def old(name):
    first_half = name[:2]
    second_half = name[2:]
    return first_half.capitalize() + second_half.capitalize()
print(old('mcdonald'))


# eg for  string manipulation
def master(text):
    wordlist = text.split()
    reverselist = wordlist[::-1]
    return reverselist
print(master('hello world this is a test'))
print(master('python programming is fun'))


#  eg for string join()
my_list = ['a','b','c']
result = 'oooooo'.join(my_list)
print(result)


my_list = ['a','b','c']
result = ' '.join(my_list)
print(result)



# let's find out absolute's  value of number using builtin function abs()

def num(n):
    return(abs(100-n) <= 10) or (abs(200-n) <= 10)
print(num(85)) #false see the condition heheh
print(num(95)) #true yayyyy!


#  LEVEL 2

# sequence of 3,3 is true
def has_33(num):
    for i in range(0,len(num)-1):
        if num[i] == 3 and num[i+1] == 3:
            return True
    return False

print("sequence=",has_33([1,3,3]))   #True
print("sequence=",has_33([1,3,1,3]))   #False



# sequence of 3,3 is true in SIMPLER FORM
def has_33(num):
    for i in range(0,len(num)-1):
        if num[i:1+2] == [3,3]:
            return True
    return False

print("sequence=",has_33([1,3,3]))   #True
print("sequence=",has_33([1,3,1,3]))   #False


# paper doll
#  return a string where every character in the original there are three characters

def paper_doll(text):
    result = " "
    for char in text:
        result += char*3
        # or
        # result += char+char+char
    return result
print(paper_doll("hello"))

# eg for same

def triple(word):
    newWord = ""
    for char in word:
        newWord += char*3
    return newWord

print("tripled=",triple("hello"))


# blackjack
def blackjack(a,b,c):
    if sum([a,b,c]) <= 21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c])-10 <= 21:
        return sum([a,b,c]) -10
    else:
        return "Bust"

print("blackjack=",blackjack(5,6,7))     #18
print(blackjack(50,9,10)) #bust


# Summer_69
def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num !=  9:
                break
            else:
                add = True
                break
    return total
print(summer_69([1,3,5]))
print(summer_69([3,6,9,5,11]))
print(summer_69([2,1,6,9,11]))