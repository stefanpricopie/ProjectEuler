def rev_collatz(x, x_steps, n):
    global x_best, most_steps, not_evaluated
    print(not_evaluated)
    if x <= n:
        not_evaluated -= 1
        if x_steps > most_steps:
            x_best, most_steps = x, x_steps
    print('x = {}, steps = {}'.format(x,x_steps))
    if not_evaluated:
        # if x is even and 3k+1, then it can be the next step for either k (odd) or for 2x
        if x % 6 == 4 and x>4: 
            rev_collatz((x-1)//3, x_steps+1, n)
        
        if x % 3 != 0 or x * 2 <= n:
            rev_collatz(2*x, x_steps+1, n)    

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    x_best = 1
    most_steps = 0
    not_evaluated = n
    rev_collatz(1, 0, n)
    print(x_best, most_steps)