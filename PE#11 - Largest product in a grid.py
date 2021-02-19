def product(vector):
    p = 1
    for x in vector:
        p *= x
    return p

grid = [[0 for i in range(26)] for i in range(3)]
for grid_i in range(20):
	grid_t = [0,0,0]+[int(grid_temp) for grid_temp in input().strip().split(' ')]+[0,0,0]
	grid.append(grid_t)
grid.extend([[0 for i in range(26)] for i in range(3)])

def best_product_pos(i,j,matrix = grid):
    S = product(matrix[i][j:j+4])
    SE = product([matrix[i][j],matrix[i+1][j+1],matrix[i+2][j+2],matrix[i+3][j+3]])
    E = product([matrix[i][j],matrix[i][j+1],matrix[i][j+2],matrix[i][j+3]])
    NE = product([matrix[i][j],matrix[i-1][j+1],matrix[i-2][j+2],matrix[i-3][j+3]])
    N = product(matrix[i][j-3:j+1])
    NV = product([matrix[i][j],matrix[i-1][j-1],matrix[i-2][j-2],matrix[i-3][j-3]])
    V = product([matrix[i][j],matrix[i][j-1],matrix[i][j-2],matrix[i][j-3]])
    SV = product([matrix[i][j],matrix[i+1][j-1],matrix[i+2][j-2],matrix[i+3][j-3]])
    return max([S,SE,E,NE,N,NV,V,SV])

m = 0
for i in range(3,23):
    for j in range(3,23):
        prod = best_product_pos(i,j)
        if prod > m:
            m = prod

print(m)