#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    list_division = []
    div = 0
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
            list_division.append(div)
        except TypeError:
            print("wrong type")
            div = 0
            list_division.append(div)
        except IndexError:
            print("out of range")
            div = 0
            list_division.append(div)
        except ZeroDivisionError:
            print("division by 0")
            div = 0
            list_division.append(div)
    return list_division
