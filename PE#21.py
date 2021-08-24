n_list = []
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    n_list.append(n)
n_max = max(n_list)

# d(n) for n between 0 and n_max-1
d_n = [0]*n_max
# amicable pair below n from 0 to n_max
amicable = [0]*(n_max+1)

def sum_div(nr):
    s = 0
    for i in range(1,nr//2+1):
        if nr % i == 0:
            s += i
    return s

# skip i=1
for i in range(2,n_max):
    # cumulative sum
    amicable[i+1] = amicable[i]
    d_n[i] = sum_div(i)
    # Ignore cases such as d(6)=6
    if d_n[i] == i:
        continue
    if d_n[i]>=n_max:
        # compute corresponding pair
        d_i = sum_div(d_n[i])
    elif d_n[d_n[i]] == 0:
        # compute and save correponding pair
        d_n[d_n[i]] = sum_div(d_n[i])
        d_i = d_n[d_n[i]]
    else:
        d_i = d_n[d_n[i]]
    if d_i == i:
        amicable[i+1] += i

for n in n_list:
    print(amicable[n])