n = int(input())
x = list(map(int,input().split()))
l = int(input())
y = list(map(int,input().split()))
k = int(input())
c = 0
for i in range(n):
    if k in range(x[i],y[i]+1):
        c+=1
print(c)