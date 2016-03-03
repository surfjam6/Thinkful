# fizzbuzz.py

n = 100
print("Fizz buzz counting up to {0}".format(n))
print("\n")

for number in range(0,n+1):
    if (number % 3 == 0) and (number % 5 ==0):
        print("FizzBuzz")
    elif (number % 3 == 0):
        print("Fizz")
    elif (number % 5 == 0):
        print("Buzz")
    else:
        print(number)
        
