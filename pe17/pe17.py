words1_9 = ['One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
words10_19 = ['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
words10x = ['Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
words20_99 = [[words10x[nr//10-2]] if nr%10==0 else [words10x[nr//10-2],words1_9[nr%10-1]] for nr in range(20,100)]

# list of lists of words
words1_99 = [[item] for item in words1_9 + words10_19] + words20_99

def abc_to_words(nr):
    if nr >= 100:
        prefix = [words1_9[nr//100-1],'Hundred']
    else:
        prefix = []
    if nr % 100 != 0:
        suffix = words1_99[nr % 100 -1]
    else:
        suffix = []
    return prefix + suffix

def nr_to_words(nr):
    if nr == 0:
        return 'Zero'
    if nr == 1000000000000:
        return 'One Trillion'
    
    str_nr = str(nr)
    groups_10power3 = []
    while str_nr:
        groups_10power3.append(str_nr[-3:])
        str_nr = str_nr[:-3]
    
    nr_list_words = []
    powers10 = [[],['Thousand'],['Million'],['Billion']]
    for i,abc in enumerate(groups_10power3):
        abc_list_words = abc_to_words(int(abc))
        if abc_list_words:
            nr_list_words = abc_to_words(int(abc)) + powers10[i] + nr_list_words
    return nr_list_words

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(*nr_to_words(n))

