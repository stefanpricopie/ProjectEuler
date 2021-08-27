t = int(input())
n_list = []
[n_list.append(int(input())) for _ in range(t)]
n_max = max(n_list)

# Sieve of Eratosthenes
primes = []
# from 0 to n_max (inclusive)
is_prime = [False]*2+[True]*(n_max-1)
# skip 0 and 1
for i in range(2,n_max+1):
    if is_prime[i]:
        primes.append(i)
        for j in range(i*i,n_max+1,i):
            is_prime[j]=False

def fast_sum_of_proper_divisors(nr):
    """
    input n, a list of primes, and a list of booleans
    returns the sum of the proper divisors
    """
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

abundants = []
sum_abundants = [False]*(n_max+1)
for nr in range(2, n_max+1):
    if fast_sum_of_proper_divisors(nr) > nr:
        abundants.append(nr)
        for a in abundants:
            if n_max < nr + a:
                break
            sum_abundants[nr+a] = True

for n in n_list:
    if sum_abundants[n]:
        print('YES')
    else:
        print('NO')