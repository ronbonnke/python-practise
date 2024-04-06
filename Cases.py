def up_low(s):
    lowercase = 0
    uppercase = 0

    for char in s:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        else:
            pass
    print(f"original string: {s}")
    print(f"Lowercase count: {lowercase}")
    print(f"Uppercase count: {uppercase}\n")
s = "Hello Mr.Rogers, how are you today??"
up_low(s)





# both are same examples see through it

# we are using dictionary here
def up_low(s):
    d = {'upper':0, 'lower':0}

    for char in s:
        if char.isupper():
            d['upper'] += 1
        elif char.islower():
            d['lower'] += 1
        else:
            pass
    print(f"original string: {s}")
    print(f"Lowercase count: {d["lower"]}")
    print(f"Uppercase count: {d["upper"]}\n")
s = "Hello Mr.Rogers, how are you today??"
up_low(s)