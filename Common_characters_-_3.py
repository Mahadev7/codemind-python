a=input()
b=a.split()
l=[]
for i in b:
    i=i.lower()
    c=list(i)
    l.append(set(c))
x=l[0]
for i in range(0,len(l)):
    x=x.intersection(l[i])
if len(x)==0:
    print('-1')
else:
    print(*min(x))