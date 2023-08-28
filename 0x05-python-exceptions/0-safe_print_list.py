#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    to_print = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            to_print += 1
        except:
            continue
    print()
    return to_print
