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