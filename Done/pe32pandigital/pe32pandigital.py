# https://www.hackerrank.com/contests/projecteuler/challenges/euler032/problem

# Brute force solution

n = int(input())

digits = list(range(1,n+1))

# 1. Generate all n-digit pandigital numbers
pandigitals = [str(d) for d in digits]

# add a digit each loop until we have n digits
for _ in range(n-1):
    new_pandigitals = []
    for d in digits:
        for p in pandigitals:
            if str(d) not in p:
                new_pandigitals.append(str(d)+p)
    pandigitals = new_pandigitals

s = 0
products = []

# 2. Check if pandigital number can be split to form a*b=c
for p in pandigitals:
    for i in range(1,n):
        for j in range(i+1,n):
            a = int(p[:i])
            b = int(p[i:j])
            c = int(p[j:])
            if a*b==c:
                if c not in products:
                    products.append(c)
                    s += c

print(s)