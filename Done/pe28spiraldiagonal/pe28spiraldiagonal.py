# https://www.hackerrank.com/contests/projecteuler/challenges/euler028/problem

mod = int(1e+9 + 7)
t = int(input())
for _ in range(t):
    k = int(input()) // 2
    
    ss1 = (2*k+1)*(2*k+2)*(4*k+3) // 6
    ss2 = k*(k+1)*(2*k+1) // 6

    # NE diagonal
    ne = (ss1 - 4*ss2) % mod
    
    # NW diagonal (exclude middle 1)
    nw = (ne - k*(k+1) - 1) % mod
    
    # SW diagonal
    sw = (nw - k*(k+1)) % mod
    
    # SE diagonal
    se = (sw - k*(k+1)) % mod
    
    print( (ne + nw + sw + se) % mod)