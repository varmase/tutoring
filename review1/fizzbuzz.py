#fizz = numbers divisible by 3
#buzz = numbers divisible by 5
#modulos: check for remainders when dividing a number. x % 3 == 0
#while loop: 

def fizzbuzz():
    check = int(input("Choose a range of numbers (starting from 1 to whatever you input) to see what numbers are a 'fizz' (divisble by 3) or a 'buzz' (divisble by 5): "))
    for i in range(1, check + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)     
while True:     
    fizzbuzz()