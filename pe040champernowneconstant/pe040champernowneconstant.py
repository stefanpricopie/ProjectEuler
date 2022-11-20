# https://www.hackerrank.com/contests/projecteuler/challenges/euler040/problem

# Solution 1: Brute force solution - 75% score (timeout)


def main():
    t = int(input())

    sets = [tuple(int(i) for i in input().split()) for _ in range(t)]

    max_d = max(max(digits) for digits in sets)

    digits_left = max_d

    n = 1
    champernowne = ''
    while digits_left > 0:
        n_str = str(n)
        champernowne += n_str
        digits = len(n_str)
        digits_left -= digits
        n += 1

    for digits in sets:
        product = 1
        for d in digits:
            product *= int(champernowne[d - 1])
        print(product)


if __name__ == '__main__':
    main()
