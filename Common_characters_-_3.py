a=input()
b=a.split()
l=[]
for i in b:
    i=i.lower()
    s=list(i)
    l.append(set(s))
z=l[0]
for i in range(0,len(l)):
    z=z.intersection(l[i])
if len(z)==0:
    print('-1')
else:
    print(min(z))