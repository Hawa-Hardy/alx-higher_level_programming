#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    x_counter = 0
    for idx in range(x):
        try:
            print("{}".format(my_list[idx]), end="")
            print()
        except IndexError:
            break
        else:
            x_counter += 1
    return x_counter