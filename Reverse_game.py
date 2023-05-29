n=int(input())
x=list(map(int,input().split()))
c=[]
for i in x:
    i=str(i)
    j=i[::-1]
    c.append(int(j))
print(*c)