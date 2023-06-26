#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i, element in enumerate(my_list):
        if count >= x:
            break
        try:
            print("{:d}".format(element), end="")
            count += 1
        except TypeError:
            pass
    print()
    return count
