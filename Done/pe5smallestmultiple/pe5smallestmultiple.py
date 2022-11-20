import math

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

def smallest_multiple(n):
    # Corner cases 
    if (n <= 1) : 
        return 1
    if (n == 2) : 
        return 2

    d = int(math.pow(2,int(math.log(n,2))) * math.pow(3,int(math.log(n,3))))

    i = 5
    while(i <= n) : 
        if isPrime(i) : 
            d *= int(math.pow(i,int(math.log(n,i))))
        i = i + 2
    
    return d

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(smallest_multiple(n))