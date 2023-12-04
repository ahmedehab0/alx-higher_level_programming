#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    divisible_check = []
    for i in my_list:
        if i % 2 == 0:
            divisible_check.append(True)
        else:
            divisible_check.append(False)
    return divisible_check
