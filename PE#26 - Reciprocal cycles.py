# https://www.hackerrank.com/contests/projecteuler/challenges/euler026/problem

def periodic_digits(n):
  idx = [0]*n
  rest = 1
  total = 1 # divisions calculated

  while True:    
    if not rest:
      return 0
      
    if idx[rest]:
      return total - idx[rest]

    idx[rest] = total
    total += 1
      
    numerator = rest * 10
    rest = numerator % n


def longest_cycle(n):
  lower = 3
  best_p = 1
  best_n = 3
  
  while n > lower:
    n -= 1
    p = periodic_digits(n)

    if p >= best_p:
      best_p = p
      best_n = n

    lower = max(lower,p+1)
  
  return best_n


t = int(input())
for _ in range(t):
    n = int(input())
    print(longest_cycle(n))
