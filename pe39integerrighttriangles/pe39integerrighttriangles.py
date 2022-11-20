# https://www.hackerrank.com/contests/projecteuler/challenges/euler039/problem

# Solution 1: Brute force solution (for max n) - 33% score (timeout)
# Solution 2: Euclid's formula for a Pythagorean triple
#             count primitive triplets only (a,b,c) - 50% score (timeout)
# Solution 3: + store best p - 100% score

import math


def main():
    t = int(input())
    ns = [int(input()) for _ in range(t)]

    max_n = max(ns)

    count = [0] * (max_n + 1)

    # Euclid's formula for a Pythagorean triple
    # a = m^2 - n^2
    # b = 2mn
    # c = m^2 + n^2
    # where m > n > 0 and m and n are coprime
    for m in range(2, int(math.sqrt(max_n)) + 1):
        for n in range(1, m):
            if (m - n) % 2 == 0 or math.gcd(m, n) != 1:
                # m and n are not coprime or m - n is even
                # if m and n are odd, then a, b and c are even (non-primitive)
                continue

            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n

            p = a + b + c
            while p <= max_n:
                count[p] += 1
                p += a + b + c

    # store best p
    best_p = [0] * (max_n + 1)
    for p in range(1, max_n + 1):
        if count[p] > count[best_p[p - 1]]:
            best_p[p] = p
        else:
            best_p[p] = best_p[p - 1]

    for n in ns:
        print(best_p[n])


if __name__ == '__main__':
    main()
