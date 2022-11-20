import math

# driver program
N = int(input().strip())

lists_digits = []

for i in range(N):
    num_digits = [int(char) for char in input().strip()]
    lists_digits.append(num_digits)

all_digits = list(map(list,zip(*lists_digits)))


first10 = 0
i = 0
while first10 < 10**9:
    first10 = first10*10 + sum(all_digits[i])
    i += 1

j = 1
N /= 10**(len(str(first10)) - 10)
while math.floor(first10+1) - first10 <= N:
    j /= 10
    first10 += sum(all_digits[i])*j
    N /= 10
    i += 1

print(math.floor(first10))