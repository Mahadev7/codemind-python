def com(x):
    a=x[0]
    b=x[1]
    c=[]
    for i in a:
        if i in b:
            c.append(i)
    if len(c)==0:
        return 0
    if len(x)==2:
        return c
    for k in range(2,len(x)):
        i=x[k]
        c1=[]
        for j in c:
            if j in i:
                c1.append(j)
        if len(c1)==0:
            return 0
        c=c1
    return c
n=input()
n=n.lower()
p=n.split()
l=com(p)
if l==0:
    print(0)
else:
    print(len(l))