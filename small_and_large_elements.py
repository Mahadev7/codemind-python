a=input()
m=a.split()
b=m[0]
c=m[-1]
l=[]
n=[]
for i in b:
    l.append(i)
for j in c:
    n.append(j)
print(min(l),max(n))