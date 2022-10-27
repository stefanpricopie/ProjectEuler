# https://www.hackerrank.com/contests/projecteuler/challenges/euler031/problem

t = int(input())

ns = [int(input()) for _ in range(t)]

max_n = max(ns)

coins = [1,2,5,10,20,50,100,200]
ways = [1] + [0]*max_n

for coin in coins:
    for i in range(coin,max_n+1):
        # ways[i] - total number of combinations with the previous coins
        # ways[i-coin] - total number of combinations with the current coin
        # starts at 1 because the current coin is the only way to make the current amount
        ways[i] += ways[i-coin]

for n in ns:
    print(ways[n]%(1e9+7))