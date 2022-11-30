n=int(input())
x=list(map(int,input().split()))
for i in range(n):
    if x[i]!=0:
        print(x[i],end=" ")
for j in range(n):
    if x[j]==0:
        print(x[j],end=' ')