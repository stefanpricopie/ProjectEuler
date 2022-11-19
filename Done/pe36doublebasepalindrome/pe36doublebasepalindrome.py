# https://www.hackerrank.com/contests/projecteuler/challenges/euler036/problem

# Solution 1: Brute force solution - 100% correct

def is_palindrome(n):
    return str(n) == str(n)[::-1]


def n_base_k(n, k):
    if n == 0:
        return '0'
    digits = []
    while n:
        n, r = divmod(n, k)
        digits.append(str(r))
    return ''.join(digits)[::-1]


if __name__ == '__main__':
    n_, k_ = map(int, input().split())

    s = 0

    for i in range(1, n_):
        if is_palindrome(i) and is_palindrome(n_base_k(i, k_)):
            s += i

    print(s)