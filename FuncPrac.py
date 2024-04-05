# function to write a volume of a sphere radius
def vol(rad):
    return (4/3)*(3.14)*(rad**3)
print(vol(2))



# this eg is for range () and len() functions
def ran_check(num,low,high):
    if num in range(low,high+1):
        print(f"{num} is within the {low} specified range {high}.")
    else:
        print("not in range")
ran_check(6,5,7)