n_list = []
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    n_list.append(n)
n_max = max(n_list)

# TIP: if a<b are amicable, then a<b<2a

# initialize to True all is_prime for n between 0 and n_max-1
is_prime = [False]*2+[True]*(2*n_max-2)
primes = [2,3]
for i in primes:
    # Sieve of Eratosthenes
    for j in range(i*i,2*n_max,i):
        is_prime[j] = False


# initialize to 0 all d(n) for n between 0 and n_max-1
d_n = [0]*n_max
# amicable pair below n from 0 to n_max
amicable = [0]*(n_max+1)

# Sieve of Eratosthenes (find primes if not enough, for fast_sum_of_proper_divisors(n))
def Sieve(n):
    for i in range(primes[-1]+2,n//2+1,2):
        if is_prime[i]:
            # Sieve of Eratosthenes
            for j in range(i*i,n_max,i):
                is_prime[j] = False
            primes.append(i)

def fast_sum_of_proper_divisors(nr):
    """
    input n, a list of primes, and a list of booleans
    returns the sum of the proper divisors
    """
    Sieve(nr)
    if is_prime[nr]:
        return 1
    nr_copy = nr
    product = 1
    for p in primes:
        if is_prime[nr_copy]:
            product *= (nr_copy**(1 + 1) - 1)//(nr_copy - 1)
            break
        if p > nr_copy:
            break
        i = 0
        while nr_copy % p == 0:
            nr_copy //= p
            i += 1
        if i != 0:
            product *= (p**(i + 1) - 1)//(p - 1)
    return product - nr

# skip i=1
for i in range(2,n_max):
    # cumulative sum
    amicable[i+1] = amicable[i]
    if d_n[i]==0:
        d_n[i] = fast_sum_of_proper_divisors(i)
    # Ignore cases such as d(6)=6
    if d_n[i] == i:
        continue
    if d_n[i] < i:
        if d_n[d_n[i]] == i:
            amicable[i+1] += i
    elif d_n[i] < n_max:
        # calculate sum of divisors if it has not been calculated yet
        if d_n[d_n[i]] == 0:
            d_n[d_n[i]] = fast_sum_of_proper_divisors(d_n[i])
        if d_n[d_n[i]] == i:
            amicable[i+1] += i
    elif d_n[i] < n_max*2:
        # calculate sum of divisors if pair is out of range
        inverse = fast_sum_of_proper_divisors(d_n[i]) 
        if inverse == i:
            amicable[i+1] += i

for n in n_list:
    print(amicable[n])