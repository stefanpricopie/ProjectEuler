# https://www.hackerrank.com/contests/projecteuler/challenges/euler033/problem?isFullScreen=true

# Solution 1: Brute force solution - 50%
# Solution 2: Use combinations of digits and gcd to iterate over possibilities
#   + Correction - Exclude all 0 cancellations (e.g. (101, 202, 11, 22), (1015, 7105, 1, 7))
#   + Correction - Ensure (numerator, denominator) pairs are counted once
#   + Correction - The leading digit of the numerator in the cancelled fraction can be zero (len(str(num2)) <= n - k)


import math


def drop_digits(num, n_digits):
    num2s = [(str(num), '')]

    for _ in range(n_digits):
        new_num2 = []
        for num2, drop in num2s:
            for i, d in enumerate(num2):
                if int(d):
                    # no zero cancellation
                    new_num2.append((num2[:i] + num2[i + 1:], ''.join(sorted(drop + d))))
        num2s = list(set(new_num2))

    return num2s


def p_is_q_without_digits(p, q, drop, n, k):
    # check if q results from dropping/cancelling drop in p
    cancel = True

    digits1 = list(str(p))

    prefix = ['0'] * (n - k - len(str(q)))
    digits2 = prefix + list(str(q))

    drop_list = list(drop)

    while digits1:
        d = digits1.pop(0)

        if digits2 and d == digits2[0]:
            digits2.pop(0)
        elif d in drop_list:
            drop_list.remove(d)
        else:
            cancel = False
            break

    return cancel


def get_denum_pairs(num, num2, drop, n, k):
    all_pairs = []

    # if num2 is zero
    if num2 == 0:
        return []

    g = math.gcd(num, num2)

    base = num // g
    base2 = num2 // g

    # denumerator is higher than numerator
    denum = num + base
    denum2 = num2 + base2

    while len(str(denum)) == n and len(str(denum2)) <= n - k:
        if p_is_q_without_digits(denum, denum2, drop, n, k):
            all_pairs.append((denum, denum2))

        denum += base
        denum2 += base2

    return all_pairs


def main(n, k):
    s_num = 0
    s_denum = 0

    sol_pairs = []

    for num in range(10 ** (n - 1), 10 ** n):
        # ensure (num, denum) pairs are unique
        other_denum = []

        for num2, drop in drop_digits(num, k):
            # get all combinations for num2 dropping k digits

            num2 = int(num2)
            for denum, denum2 in get_denum_pairs(num, num2, drop, n, k):
                # add if denum not already in other_denum
                if denum not in other_denum:
                    s_num += num
                    s_denum += denum

                    sol_pairs.append((num, denum))
                    # add denum to other_denum
                    other_denum.append(denum)

    return s_num, s_denum


if __name__ == '__main__':
    a, b = [int(i) for i in input().split()]

    print(*main(a, b))

