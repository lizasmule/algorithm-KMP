def kmpSearchByCompil(s, x):
    d = {0:0}
    template = x + '#' + s
    for i in range(1,len(template)):
        j = d[i-1]
        while j > 0 and template[j] != template[i]:
            j = d[j-1]
        if template[j] == template[i]:
            j += 1
        d[i] = j
        if j == len(x):
            return i
    return 0

# print (kmpSearchByCompil("ababcabab", "ab"))