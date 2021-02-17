def product_triplet(a,n):
    b = n*(n-2*a)/(2*(n-a))

    if not b.is_integer():
        return -1

    c = n - a - b
    if a**2 + b**2 == c**2:
        return int(a*b*c)
    return -1

def best_triplet(n):
    p = -1
    for a in range(1,n//3 + 1):
        new_p = product_triplet(a,n)
        if new_p > p:
            p = new_p
    return p

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(best_triplet(n))