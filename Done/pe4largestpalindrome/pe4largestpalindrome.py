def palindrom(abc):
    a,b,c = [char for char in str(abc)]
    return int(a+b+c+c+b+a)

def first_palindrom(n):
    root = n//1000
    pali = palindrom(root)
    if pali < n:
        return pali
    else:
        return palindrom(root-1)

def is_prime(pali):
    if pali%999 == 0:
        return False
    else:
        s_div = pali//999 + 1
        if pali%s_div == 0:
            return False
        else:
            b_div = pali//s_div
            while s_div < b_div:
                s_div += 1
                if pali%s_div == 0:
                    return False
                b_div = pali//s_div
            return True

def large_palindrom(n):
    pali = first_palindrom(n)
    root = pali//1000
    
    while is_prime(pali):
        root -= 1
        pali = palindrom(root)
    
    return pali

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(large_palindrom(n))