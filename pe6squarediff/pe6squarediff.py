import math

def ssd(n):
    return  int(math.pow(n*(n+1)//2,2)) - n*(n+1)*(2*n+1)//6

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(ssd(n))