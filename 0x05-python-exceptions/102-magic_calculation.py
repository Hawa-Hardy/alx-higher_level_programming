#!/usr/bin/python3
def magic_calculation(a, b):
    sum = 0
    for idx in range(1, 3):
        try:
            if (idx > a):
                raise Exception("Too far")
            else:
                sum += (a ** b) / idx
        except:
            sum = b + a
            break
    return (sum)
