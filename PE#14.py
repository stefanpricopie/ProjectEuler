def collatz(x):
    global nr_steps
    if x in nr_steps:
        return nr_steps[x]
    else:
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

nr_steps = {1: 0}
for i in range(1,n_max+1):
    if i not in nr_steps:
        collatz(i)

results = list({ your_key: nr_steps[your_key] for your_key in range(1,n_max+1) }.values())
results.reverse()

for n in n_list:
    slice = results[-n:]
    print(n - slice.index(max(slice)))