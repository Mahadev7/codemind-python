def madam(n):
    a=n[0]
    b=n[1]
    c=[]
    for i in a:
        if i in b:
            c.append(i)
    if len(c)==0:
        return 0
    if len(n)==2:
        return c
    for k in range(2,len(n)):
        i=n[k]
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
l=madam(p)
if l==0:
    print('-1')
else:
    print(''.join(l))