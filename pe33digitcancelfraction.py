# https://www.hackerrank.com/contests/projecteuler/challenges/euler033/problem?isFullScreen=true

n, k = [int(i) for i in input().split()]

s_num = 0
s_denum = 0

for num in range(10**(n-1), 10**n):
    for denum in range(num+1, 10**n):
        # get all pairs with k canceling digits
        pairs = [(str(num), str(denum))]

        for _ in range(k):
            new_pairs = []
            for num_str, denum_str in pairs:
                for i in range(len(num_str)):
                    if num_str[i] == '0':
                        continue

                    for j in range(len(denum_str)):
                        if num_str[i] == denum_str[j]:
                            new_num_str = num_str[:i] + num_str[i+1:]
                            new_denum_str = denum_str[:j] + denum_str[j+1:]
                            if new_num_str and new_denum_str and (new_num_str, new_denum_str) not in new_pairs:
                                new_pairs.append((new_num_str, new_denum_str))
            pairs = new_pairs

        # check if the fraction is equal to the original one
        for num_str, denum_str in pairs:
            new_num = int(num_str)
            new_denum = int(denum_str)

            if new_denum and new_num/new_denum == num/denum:
                s_num += num
                s_denum += denum
                break

print(s_num, s_denum)