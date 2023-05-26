n=input()
d={}
a=[]
for i in n:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i,j in d.items():
    if j==1:
        a.append(i)
if len(a)==0:
    print('-1')
else:
    print(a[0])