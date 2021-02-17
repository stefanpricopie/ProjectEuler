def sum_even(n):
    if n<2:
        return 0
    else:
        a = 1
        b = 2
        s = 0
        while b<=n:
            s += b
            a, b = a+2*b, 2*a+3*b
    return s

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    print(sum_even(n))