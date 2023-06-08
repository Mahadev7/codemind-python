n=int(input())
x=list(map(int,input().split()))
p=[]
for i in range(len(x)):
    for j in range(i,len(x)):
        s=x[i:j+1]
        p.append(s)
a=[]
for i in p:
    c=sum(i)
    a.append(c)
print(max(a))