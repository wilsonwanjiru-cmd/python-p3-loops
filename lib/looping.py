#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i >= 1:
        print(i)
        i -= 1
    print("Happy New Year!")

def square_integers(int_list):
    squared_numbers = [num ** 2 for num in int_list]
    return squared_numbers

def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

# Uncomment the following line to test each function individually
# happy_new_year()
# result = square_integers([1, 2, 3, 4, 5])
# fizzbuzz()
