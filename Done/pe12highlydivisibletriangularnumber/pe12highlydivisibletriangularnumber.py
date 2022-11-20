prime = [2]

# driver program 
t = int(input().strip())
n_list = []
for a0 in range(t):
    n = int(input().strip())
    n_list.append(n)
n_max = max(n_list)

# Max triangular
m_tri = [0 for i in range(n_max+1)]

def count_div(n):
    if n==1:
        return 1
    count = 1

    for i in prime:
        new = 1
        while n%i == 0:
            n //= i
            new += 1
        count *= new
    if n != 1:
        prime.append(n)
        count *= 2
    return count

a = 1
best_div = 1

while best_div <= n_max:
    tri = a*(a+1)//2
    d = count_div(tri)

    if d > best_div:
        for i in range(best_div, min([d,n_max+1]) ):
            m_tri[i] = tri
        best_div = d

    a += 1

for n in n_list:
    print(m_tri[n])