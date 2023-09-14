#!/usr/bin/python3
"""a function that returns a list of lists
of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """ a function representing the Pascal’s triangle of n"""

    tria = []
    if n <= 0:
        return tria
    tria = [[1]]
    while len(tria) != n:
        tri = tria[-1]
        ptem = [1]
        for i in range(len(tri) - 1):
            ptem.append(tri[i] + tri[i + 1])
        ptem.append(1)
        tria.append(ptem)
    return tria
