#!/usr/bin/python3
def fizzbuzz():
    for nums in range(1, 100+1):
        if nums % 3 == 0 and nums % 5 == 0:
            print("FizzBuzz ", end="")
        elif nums % 3 == 0:
            print("Fizz ", end="")
        elif nums % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(nums), end="")
