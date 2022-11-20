# Memoisation is an optimization technique used primarily to speed up computer programs
# by storing the results of expensive function calls and returning the cached result
# when the same inputs occur again.

t = int(input().strip())
n_list = []
for a0 in range(t):
    n = int(input().strip())
    n_list.append(n)
n_max = max(n_list)

nr_steps = [0]*n_max

def collatz(x):
    if x == 1:
        return 0
    if x <= n_max:
        if nr_steps[x-1]:
            return nr_steps[x-1]

    if x % 2 == 0:
        x_step = 1 + collatz(x//2)
    else:
        x_step = 1 + collatz(3*x+1)

    if x <= n_max:
        # store result globally
        nr_steps[x-1] = x_step
    return x_step

for i in range(1,n_max+1):
    if not nr_steps[i-1]:
        collatz(i)

results = [(0,1)]
for x,x_step in enumerate(nr_steps[1:]):
    results.append(max(results[-1] , (x_step,x+2)))

for n in n_list:
    print(results[n-1][1])