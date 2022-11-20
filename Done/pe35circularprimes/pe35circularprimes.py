# https://www.hackerrank.com/contests/projecteuler/challenges/euler035/problem?isFullScreen=true

# Solution 1: Brute force solution - 80% timeout
# Solution 2: Sieve of Eratosthenes - 100%

def rotations(nr):
    s = str(nr)
    return [int(s[i:] + s[:i]) for i in range(len(s))]


def sieve_of_eratosthenes(nr):
    prime = [True for _ in range(nr + 1)]

    p = 2
    while p * p <= nr:

        # If prime[p] is not changed, then it is a prime
        if prime[p]:

            # Update all multiples of p
            for i in range(p * 2, nr + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False

    # return prime vector
    return prime


if __name__ == '__main__':
    n = int(input())

    check_prime = sieve_of_eratosthenes(int('9' * len(str(n))))

    sum_circular_primes = 0

    for ni in range(1, n):
        if all([check_prime[r] for r in rotations(ni)]):
            sum_circular_primes += ni

    print(sum_circular_primes)
