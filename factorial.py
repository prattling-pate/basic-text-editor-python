import sys

"""
This was all written using my own text editor!!!

This is so cool!!!
"""

def factorial(n : int):
    if n<=1:
        return 1
    return n*factorial(n-1)

def choose(n : int, c : int):
    return factorial(n)/(factorial(n-c)*factorial(c))

def pascals_triangle(n : int):
    lists = []
    for i in range(1,n):
        lists.append([])
        for j in range(n):
            if i >= j:
                lists[i-1].append(choose(i,j))
        print(lists[i-1])

n = int(sys.argv[1])

pascals_triangle(n)
