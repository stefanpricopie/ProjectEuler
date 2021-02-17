def sumof35(n):
    d3 = (n-1)//3
    s = ((d3*(d3+1))//2)*3

    d5 = (n-1)//5
    s += ((d5*(d5+1))//2)*5

    d15 = (n-1)//15
    s -= ((d15*(d15+1))//2)*15

    return s

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sumof35(n))