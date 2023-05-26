n=int(input())
x=list(map(int,input().split()))
a=[]
b=[]
for i in x:
    if i in a:
        pass
    else:
        s=x.count(i)
        a.append(i)
        b.append(i)
        b.append(s)
print(*b)