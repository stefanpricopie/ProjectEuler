# https://www.hackerrank.com/contests/projecteuler/challenges/euler039/problem

# Solution 1: Brute force solution (for max n) - 33% score (timeout)

import math


def main():
    t = int(input())
    ns = [int(input()) for _ in range(t)]

    max_n = max(ns)

    count = [0] * (max_n + 1)

    # assume a < b < c
    for a in range(1, math.ceil(max_n/(2 + math.sqrt(2)))):
        for b in range(a+1, math.ceil(max_n/2)):
            c = math.sqrt(a**2 + b**2)
            if c.is_integer():
                p = a + b + int(c)
                if p <= max_n:
                    count[p] += 1

    for n in ns:
        max_triangles = max(count[:n+2])
        print(count.index(max_triangles))


if __name__ == '__main__':
    main()
