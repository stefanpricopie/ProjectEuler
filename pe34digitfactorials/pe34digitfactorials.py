# https://www.hackerrank.com/contests/projecteuler/challenges/euler034/problem?isFullScreen=true

# Solution 1: Brute force solution - 100%

import math


def is_curious(nr):
    s = sum([math.factorial(int(d)) for d in str(nr)])
    return s % nr == 0


if __name__ == '__main__':
    n = int(input())

    sum_curious = 0

    for i in range(10, n):
        if is_curious(i):
            sum_curious += i

    print(sum_curious)
