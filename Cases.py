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