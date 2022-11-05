# https://www.hackerrank.com/contests/projecteuler/challenges/euler035/problem?isFullScreen=true

# Solution 1: Brute force solution - 80% timeout

def nr_rotations(nr):
    s = str(nr)
    return [int(s[i:] + s[:i]) for i in range(len(s))]


def is_prime(nr):
    if nr == 1:
        return False
    if nr == 2:
        return True
    if nr % 2 == 0:
        return False
    for i in range(3, int(nr**0.5) + 1, 2):
        if nr % i == 0:
            return False
    return True


def is_circular_prime(nr):
    return all([is_prime(r) for r in nr_rotations(nr)])


if __name__ == '__main__':
    n = int(input())

    sum_circular_primes = 0

    for i in range(1, n):
        if is_circular_prime(i):
            sum_circular_primes += i

    print(sum_circular_primes)
