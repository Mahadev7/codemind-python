n=int(input())
x=list(map(int,input().split()))
s=[]
i=0
j=n-1
while i<=j:
    if i==j:
        s.append(x[i])
        s.append(0)
        break
    s.append(x[i])
    s.append(x[j])
    i+=1
    j-=1
print(*s)