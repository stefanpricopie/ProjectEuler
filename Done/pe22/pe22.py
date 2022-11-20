names = ['']
def find_position(name,lower,upper):
    while lower < upper-1:
        half = (lower+upper)//2
        if name < names[half]:
            upper = half
            find_position(name,lower,upper)
        elif name > names[half]:
            lower = half
            find_position(name,lower,upper)
        else:
            return half
    return upper

# sort names
N = int(input())
for i in range(N):
    name = input()
    names.insert(find_position(name,0,len(names)),name)

# return queries
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letter_to_nr = {letter:i+1 for i,letter in enumerate(alphabet)}

def value_name(name):
    return sum([letter_to_nr[l] for l in name])

Q = int(input())
for _ in range(Q):
    name = input()
    print(find_position(name,0,N+1)*value_name(name))