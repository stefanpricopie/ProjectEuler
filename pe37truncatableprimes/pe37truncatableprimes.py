# https://www.hackerrank.com/contests/projecteuler/challenges/euler037/problem

# Solution 1: Brute force solution - 100% correct

def is_prime(n):
    if n <= 1:
        return False

    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6

    return True


def truncate_l(n):
    return [int(str(n)[i:]) for i in range(1, len(str(n)))]


def truncate_r(n):
    return [int(str(n)[:i]) for i in range(1, len(str(n)))]


if __name__ == '__main__':
    n_ = int(input())

    truncatable_primes = []

    nr = 10
    while nr < n_:
        if is_prime(nr):
            if all([is_prime(j) for j in truncate_l(nr)]) and all([is_prime(j) for j in truncate_r(nr)]):
                truncatable_primes.append(nr)
        nr += 1

    print(sum(truncatable_primes))
