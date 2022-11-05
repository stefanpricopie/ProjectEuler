# https://www.hackerrank.com/contests/projecteuler/challenges/euler030/problem

n = int(input())

s = 0

m = 9**n

for nr in range(10, m*len(str(m))):
    s += nr if nr == sum([int(digit)**n for digit in str(nr)]) else 0

print(s)