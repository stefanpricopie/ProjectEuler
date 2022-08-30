def adj_sum(i,j,sum,n):
    global max
    if i + 1 == n:
        if sum > max:
            max = sum
    else:
        adj_sum(i+1, j, sum + triangle[i+1][j], n)    
        adj_sum(i+1, j+1, sum + triangle[i+1][j+1], n)    

t = int(input().strip())
for t0 in range(t):
    n = int(input().strip())
    triangle = []
    max = 0
    for j in range(n):
        triangle.append([int(k) for k in input().split()])
    adj_sum(0,0,triangle[0][0],n)
    print(max)