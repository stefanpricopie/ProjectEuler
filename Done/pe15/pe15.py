from math import factorial as fact

def combinatorial(n,k):
    return (fact(n) // (fact(k) * fact(n-k))) % 1000000007

t = int(input().strip())
for a0 in range(t):
    m,n = [int(i) for i in input().strip().split(' ')]
    print(combinatorial(m+n,m))