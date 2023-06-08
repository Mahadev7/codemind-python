a=int(input())
b=int(input())
l=[]
p=[]
for i in range(a,b+1):
    l.append(i)
for i in range(len(l)):
    for j in range(i,len(l)):
        s=l[i:j+1]
        p.append(s)
# print(p)
q=0
for i in p:
    c =sum(i)
    if c%2!=0:
        q+=1
print(q)