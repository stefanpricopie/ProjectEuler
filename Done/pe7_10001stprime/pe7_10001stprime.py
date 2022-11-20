def isPrime(n) : 
 
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
 
    # This is checked so that we can skip 
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
 
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
 
    return True

prime_list = [2,3,5,7,11,13,17,19,23,29]

def get_prime(n):
    primes = len(prime_list)
    if n <= primes:
        return prime_list[n-1]
    else:
        p = prime_list[-1]
        while primes < n:
            p += 2
            if isPrime(p):
                prime_list.append(p)
                primes += 1
        return p

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(get_prime(n))