n = int(input())
arr = list(map(int,input().split()))
d = {}
l = []
for i in arr:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i,j in d.items():
    if j == 1:
        l.append(i)
if len(l) == 0:
    print("-1")
else:
    print(max(l))