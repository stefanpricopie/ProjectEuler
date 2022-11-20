# https://www.hackerrank.com/contests/projecteuler/challenges/euler027/problem

def isprime(n):
    # Corner cases
    if n <= 1:
        return False
    if n <= 3:
        return True

    # This is checked so that we can skip 
    # middle five numbers in below loop 
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6

    return True


def quadratic(n, a, b):
    return n * n + a * n + b


def consec_primes(a, b):
    count = 0
    fn = quadratic(count, a, b)

    while isprime(fn):
        count += 1
        fn = quadratic(count, a, b)

    return count


def best_quadratic_prime(n):
    bs = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]  # b must be a (positive) prime

    # add all primes up to n
    b = 43
    while b < n:
        if isprime(b):
            bs.append(b)
        b += 2

    best_pair = (1, 41)
    most_primes = 40

    for a in range(-n, n + 1):
        for b in bs:

            n_primes = consec_primes(a, b)

            if n_primes > most_primes:
                most_primes = n_primes
                best_pair = (a, b)

    return best_pair


if __name__ == '__main__':
    nr = int(input())
    print(*best_quadratic_prime(nr))
