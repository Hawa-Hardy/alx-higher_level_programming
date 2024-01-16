#!/usr/bin/python3
for first in range(0, 10):
    for col in range(first + 1, 10):
        if first == 8 and col == 9:
            print('89')
        else:
            print('{}{}, '.format(first, col), end='')
