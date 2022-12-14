a=list(map(str,input().split()))
b=list(map(str,input().split()))
d=[]
e=[]
c=0
for i in a:
    i=i.lower()
    d.append(i)
for j in b:
    j=j.lower()
    e.append(j)
for i in d:
    if i in e:
        c+=1
print(c)