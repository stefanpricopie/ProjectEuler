# https://www.hackerrank.com/contests/projecteuler/challenges/euler040/problem

# Solution 1: Brute force solution - 75% score (timeout)
# Solution 2: Use the fact that the number of digits in the number is known - 100% score

from bisect import bisect

start_digit = [0, 1, 21, 321, 4321, 54321, 654321, 7654321, 87654321, 987654321, 10987654321,
               120987654321, 1320987654321, 14320987654321, 154320987654321, 1654320987654321,
               17654320987654321, 187654320987654321, 1987654320987654321]


def champernowne_digit(n):
    """
    1-9: 9 * 1 digits
    10-99: 90 * 2 digits
    100-999: 900 * 3 digits
    ...
    1e17-(1e18-1): 9*1e17 * 18 digits
    """
    div = (n-1) // 9

    # Find the number of digits in the number
    nr_digits = bisect(start_digit, div)

    low = start_digit[nr_digits - 1] * 9

    d, r = divmod(n - low, nr_digits)

    nr = 10**(nr_digits - 1) - 1 + d

    if r == 0:
        return nr % 10
    else:
        return int(str(nr+1)[r-1])


def main():
    t = int(input())
    for _ in range(t):
        group = list(map(int, input().split()))
        product = 1
        for n in group:
            product *= champernowne_digit(n)
        print(product)


if __name__ == '__main__':
    main()
