def product(a_list):
    if 0 in a_list:
        return 0
    p = a_list[0]
    for elem in a_list[1:]:
        p *= elem
    return p

def max_product(n_list,k):
    m = prod = product(n_list[:k])
    
    i = 0
    while i < len(n_list) - k:
        if prod != 0:
            prod = (prod*n_list[i+k])//n_list[i]
            if prod > m:
                m = prod
        elif 0 not in n_list[i+1:i+k+1]:
            prod = product(n_list[i+1:i+k+1])
            if prod > m:
                m = prod
        i+=1
    return m

t = int(input().strip())
for a0 in range(t):
    n,k = [int(i) for i in input().strip().split(' ')]
    num = input().strip()
    n_list = [int(char) for char in num]
    print(max_product(n_list,k))
