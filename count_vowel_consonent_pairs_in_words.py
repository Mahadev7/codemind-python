def fun(n):
    a=[]
    x='AEIOUaeiou'
    y='BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
    i=0
    j=len(n)-1
    while i<j:
        if (n[i] in x and n[j] in y) or (n[i] in y and n[j] in x):
            a.append((n[i],n[j]))
        i+=1
        j-=1
    return len(a)
n=input()
l=[]
p=n.split()
for i in p:
    z=fun(i)
    l.append(z)
print(sum(l))