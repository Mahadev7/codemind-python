n  = input()
d = {}
l = []
for i in n:
    if i not in d:
        d[i] = 1
    else:
        d[i]+=1
for i,j in d.items():
    if j == 1:
        l.append(i)
if len(l)==0:
    print('-1')
else:
    print(l[0])