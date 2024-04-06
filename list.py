
# let's print the list in SET format
def u_list(li):
    return list(set(li))
print(u_list([1,1,7,1,2,2,6,2,3,4,4,5,6,9,8])) # gives in Ordered way

# same results with a placeholder x
def u_list(li):
    xox = []
    for num in li:
        if num not in xox:
            xox.append(num)
    return xox
print(u_list([1,1,7,1,2,2,6,2,3,4,4,5,6,9,8])) # gives in unordered way


def multiply(num):
    total = 1
    for x in num:
        total = total * x
    return total
print(multiply([1,2,3,-4,10]))
