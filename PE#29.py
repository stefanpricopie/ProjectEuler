n = int(input())
nr = 0
powers = [(i,1) for i in range(n+1)]
# from 0 to n_max (inclusive)
is_prime = [False]*2+[True]*(n-1)

def count_power(a,b,n=n):
    if a<b:
        if is_prime[b]:
            return True
        # find a<c,d<b
        root, power = powers[a]
        power_root = b*power  # power of the root

        c = a*root
        power += 1
        while c <= n:
            if power_root % power == 0:
                d = power_root//power
                if max(c,d) < max(a,b):
                    return False
                else:
                    return True
            c *= root
            power += 1
        return True

    if a>b:
        # find c<a,b<d
        root, power = powers[a]
        if power == 1:
            # if root of a is a (i.e. power = 1)
            return True
        power_root = b*power  # power of the root
        
        c = a//root
        power -= 1
        while power_root//power <= n:
            if power_root % power == 0:
                d = power_root//power
                if max(c,d) <= max(a,b):
                    return False
                else:
                    return True
            c //= root
            power -= 1
            if power == 0:
                break
        return True

for i in range(2,n+1):
    nr +=1  # for i^i
    for j in range(2,i):
        if count_power(j,i):
            nr += 1
        if count_power(i,j):
            nr += 1

    if powers[i][1] == 1:
        # powers
        j = i*i
        power = 2
        while j <= n:
            powers[j] = (i,power)
            j *= i
            power += 1
        # primes
        if is_prime[i]:
            for j in range(i*i,n+1,i):
                is_prime[j]=False

print(nr)