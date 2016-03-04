# fizzbuzz.py
import sys

min = 0
maximum = 100

if len(sys.argv) > 1:
    try:
        max = int(sys.argv[1])
    except ValueError:
        max = -1
else:
    max = -1

if max < 0:
    try:
        max = int(input("Enter max range\n"))
    except ValueError:
        max = maximum

print("Fizz buzz counting up to {0}".format(max))
print("\n")

for number in range(min,max+1):
    if (number % 3 == 0) and (number % 5 ==0):
        print("FizzBuzz")
    elif (number % 3 == 0):
        print("Fizz")
    elif (number % 5 == 0):
        print("Buzz")
    else:
        print(number)
