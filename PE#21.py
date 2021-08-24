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
    if d_n[i] == 0:
        d_n[i] = sum_div(i)
    # compute d_n of pair if does not exist
    if d_n[i]<n_max and d_n[i]!=i:
        if d_n[d_n[i]] == 0:
            d_n[d_n[i]] = sum_div(d_n[i])
        # check if amicable
        if d_n[d_n[i]] == i:
            amicable[max(i,d_n[i])+1] = i + d_n[i]
    # cumulative sum
    amicable[i+1] += amicable[i]

for n in n_list:
    print(amicable[n])