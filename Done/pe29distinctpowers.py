# https://www.hackerrank.com/contests/projecteuler/challenges/euler029/problem

n = int(input())

def coprimes(a_list):   # returns list such that there are no a,b with a%b == 0
    i = 0
    while i < len(a_list)-1:
        j = i+1
        while j < len(a_list):
            if a_list[j] % a_list[i] == 0:
                del a_list[j]
            j +=1
        i += 1
    return a_list

def is_multiple(nr,divisors):
    for div in divisors:
        if nr % div == 0 and nr != div:
            return True
    return False

def count_powersofroot(max_power, n = n):
    nr = 0
    power = 1
    while power < max_power:
        root_powers = [power*i for i in range(2,n+1)]
        divisors = coprimes(list(range(power+1,max_power+1)))
        # remove powers that can be expressed by a higher power of the root
        count_powers = len([root for root in root_powers if not is_multiple(root,divisors)])
        nr += count_powers
        power += 1
    # count all root powers of maximum root
    nr += n-1
    return nr

nr = 0
# from 0 to n
powers = [(i,1) for i in range(n+1)]
# from 0 to log2(n)+1
nrroots_by_power = [0]*n.bit_length()

for i in range(2,n+1):
    if powers[i][1] == 1:
        # powers
        j = i*i
        power = 2
        while j <= n:
            powers[j] = (i,power)
            j *= i
            power += 1
        power -= 1
        if nrroots_by_power[power] == 0:
            nrroots_by_power[power] = count_powersofroot(power)
        nr += nrroots_by_power[power]
print(nr)