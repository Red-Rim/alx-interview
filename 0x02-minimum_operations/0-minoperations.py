#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """ Calculate the minimum number of operations needed to achieve n characters """
    if n <= 1:
        return 0
    
    i = 2
    c = 0
    while i <= n:
        if n % i == 0:
            c += i
            n = n / i
        else:
            i += 1

    if c == 0:
        return 0

    return c

if __name__ == "__main__":
    n = 4
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
