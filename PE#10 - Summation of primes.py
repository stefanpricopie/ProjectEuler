# Python program to print all primes smaller than or equal to 
# n using Sieve of Eratosthenes 

def cumsum(it):
    total = 0
    for x in it:
        total += x
        yield total
  
def SieveOfEratosthenes(n): 
      
    # Create a boolean array "prime[0..n]" and initialize 
    # all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False

    # return prime vector
    return prime 
  
# driver program 
t = int(input().strip())
n_list = []
for a0 in range(t):
    n = int(input().strip())
    n_list.append(n)
    n_max = max(n_list)

prime = SieveOfEratosthenes(n_max)
prime_or_zero = [i if p else 0 for i,p in enumerate(prime)]
prime_sums = list(cumsum(prime_or_zero))

for n in n_list:
    print(prime_sums[n])