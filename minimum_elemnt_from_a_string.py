a=input()
b=a.split()
c=b[-1]
d=list(c)
p=min(d)
l=[]
for i in d:
    if p.lower()==i:
        l.append(i)
if len(l)==0:
    print(p)
else:
    print(l[0])