n=int(input())
x=list(map(int,input().split()))
s=0
for i in x:
    i=str(i)
    for j in i:
        s+=int(j)
print(s)