#def rec(): looping function
#rec(): how to call def rec():
#recursive v. non-recursive: recursive calls function inside itself
#set number to power using recursive call
#base cannot be changed, must stay same

def power(base, exponent):
    if exponent == 0:
        return 
    return base * power(base, exponent-1)
print(power(2, 3))