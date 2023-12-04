#!/usr/bin/python3

"""pascal triangle module"""


def pascal_triangle(n):
    """function that returns a list of lists of integers representing
    the Pascal’s triangle of n

    Args:
        n: integer

    Return:
        list of integres or empyt list if n <= 0
    """

    if n <= 0:
        return []

    pascal = []
    for i in range(1, n + 1):
        row = []
        z = 0
        for j in range(i):
            if j == i - 1 or j == 0:
                row.append(1)
                continue
            if z <= (len(pascal[i-2]) - 1):
                row.append(pascal[i - 2][z] + pascal[i-2][z+1])
                z += 1
        pascal.append(row)
    return pascal
