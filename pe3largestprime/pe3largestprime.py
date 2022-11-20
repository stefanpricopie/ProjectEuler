def larg_prime_div(n):
    while n%2 == 0:
        n = n//2
    if n == 1:
        return 2
    else:
        d=3
        while d*d <= n:
            while n%d == 0:
                n = n//d
            d += 2
        if n == 1:
            return d-2
        else:
            return n

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(larg_prime_div(n))