r=int(input())
c=int(input())
s=0
for i in range(r):
    x=list(map(int,input().split()))
    for  i in range(c):
        s+=x[i]
print(s)