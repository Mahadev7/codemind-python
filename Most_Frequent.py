n = int(input())
x = list(map(int,input().split()))
d = {}
l,z = [],[]
for i in x:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for j in d.values():
    l.append(j)
p = max(l)
for i in x:
    if x.count(i)==p:
        z.append(i)
if len(z)>1:
    print(min(z))
else:
    print(*z)