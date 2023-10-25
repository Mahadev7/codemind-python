# aabababa 
a = input()
a1 = [i for i in a if i.isalpha()]
d = {}
l,l2 = [],[]
for i in a1:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i,j in d.items():
    l.append(j)
p = max(l)
for i in a1:
    if a1.count(i)!=p:
        l2.append(i)
        print(*l2)
        break
else:
    print(-1)