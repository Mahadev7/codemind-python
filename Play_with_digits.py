n=int(input())
arr=list(map(int,input().split()))
c=0
for i in arr:
    i=str(i)
    for j in i:
        c+=int(j)
print(c)