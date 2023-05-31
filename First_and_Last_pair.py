n=int(input())
x=list(map(int,input().split()))
i=0
j=n-1
l=[]
while i<=j:
    if i==j:
        l.append(x[i])
        l.append(0)
        break
    l.append(x[i])
    l.append(x[j])
    i+=1
    j-=1
print(*l)