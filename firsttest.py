number1 = input("Pick a number between 1-100: ")

number = int(number1)
if number%3==0:
    print ("Fizz")
elif number % 3 == 0 and number % 5 == 0:
    print("Fizzbuzz")

elif  number%5==0:
    print ("buzz")

else:
    print("Nope")
