# Memoisation is an optimization technique used primarily to speed up computer programs
# by storing the results of expensive function calls and returning the cached result
# when the same inputs occur again.

nr_steps = {1:0}

def collatz(x):
    if x in nr_steps:
        return nr_steps[x]

    if x % 2 == 0:
        x_step = 1 + collatz(x//2)
    else:
        x_step = 1 + collatz(3*x+1)
    # store result globally
    nr_steps[x] = x_step
    return x_step

t = int(input().strip())
n_list = []
for a0 in range(t):
    n = int(input().strip())
    n_list.append(n)
n_max = max(n_list)

for i in range(1,n_max+1):
    if i not in nr_steps:
        collatz(i)

all_steps = list({ your_key: nr_steps[your_key] for your_key in range(1,n_max+1) }.values())
results = [(0,1)]
for x,x_step in enumerate(all_steps[1:]):
    results.append(max(results[-1] , (x_step,x+2)))

for n in n_list:
    print(results[n-1][1])