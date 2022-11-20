# https://www.hackerrank.com/contests/projecteuler/challenges/euler038/problem

# Solution 1: Brute force solution - 100% correct

def unique_char(n_str):
    return len(n_str) == len(set(n_str))


def multiple_pandigital(m, k):
    digits = set([str(d) for d in range(1, k+1)])

    n = m

    while digits:
        n_str = str(n)
        if not unique_char(n_str) or not set(n_str).issubset(digits):
            return False

        digits -= set(n_str)
        n += m

    return True


def main():
    n, k = map(int, input().split())

    for nr in range(2, n):
        if multiple_pandigital(nr, k):
            print(nr)


if __name__ == '__main__':
    main()
