def fun(q):
    p=list(q)
    l=[]
    for i in range(len(p)):
        if p[i].isalnum():
            l.append(p[i])
            p[i]='*'
    l.sort()
    for i in range(len(p)):
        if p[i]=='*':
            p[i]=l[0]
            l.pop(0)
    return p
            
a=input()
b=a.split()
for i in b:
    z=fun(i)
    print("".join(z),end=' ')
            