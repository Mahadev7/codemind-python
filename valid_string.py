def Valid(n):
    d = {}
    l = []
    for i in n:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    for j in d.values():
        l.append(j)
    s = set(l)
    if len(s)==1:
        return "Valid String"
    elif len(s)==2:
        if l.count(1) == 1 and 1 in s:
            return "Valid String"
    return "Not Valid"
n = input()
print(Valid(n))