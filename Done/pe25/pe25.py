t = int(input())
n_list = []
for _ in range(t):
    n_list.append(int(input()))
n_max = max(n_list)

results = [0]*(n_max+1)

precision = 1e5

a = b = 1
i = 2
digits = 1
while digits < n_max:
    a, b = b, a+b
    i += 1
    if len(str(int(a))) < len(str(int(b))):
        digits += 1
        if digits in n_list:
            results[digits] = i
        if b > precision:
            b /= 10
            a /= 10

for n in n_list:
    print(results[n])