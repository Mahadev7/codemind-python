import math
n=int(input())
x=list(map(int,input().split()))
p=x[0]
for i in range(len(x)):
    p=math.gcd(p,x[i])
print(p)