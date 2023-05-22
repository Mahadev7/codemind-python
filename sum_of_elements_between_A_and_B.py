n=int(input())
x=list(map(int,input().split()))
a,b=map(int,input().split())
s=0
for i in range(len(x)):
    if x[i]>=a and x[i]<=b:
        s+=x[i]
print(s)