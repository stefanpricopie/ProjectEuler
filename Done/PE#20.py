from math import factorial

def sum_digits(nr):
    s = 0
    for digit in str(nr):
        s += int(digit)
    return s

t = int(input().strip())
for t0 in range(t):
    n = int(input().strip())
    print(sum_digits(factorial(n)))