t = int(input().strip())
n_list = []
for a0 in range(t):
    n = int(input().strip())
    n_list.append(n)
n_max = max(n_list)

sum_digits = [0]*n_max

def sum_d(nr):
    sum_of_digits = 0
    for digit in str(nr):
        sum_of_digits += int(digit)
    return sum_of_digits

nr = 1
for i in range(1, n_max+1):
    nr*=2
    if i in n_list:
        sum_digits[i-1] = sum_d(nr)

for n in n_list:
    print(sum_digits[n-1])