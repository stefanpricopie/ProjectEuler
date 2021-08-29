import math

t = int(input())
lex = []
alphabet = 'abcdefghijklm'
for _ in range(t):
    # transform 1-index in 0-index
    n = int(input())-1
    lex.append((n,[letter for letter in alphabet].copy(),''))

div = math.factorial(len(alphabet)-1)

for d in range(len(alphabet)-1,0,-1):
    for i in range(t):
        n, rest_letters, word = lex[i]
        index = n//div
        word += rest_letters[index]
        del rest_letters[index]
        n %= div
        lex[i] = n, rest_letters, word
    div //= d

for i in range(t):
    print(lex[i][2]+lex[i][1][0])