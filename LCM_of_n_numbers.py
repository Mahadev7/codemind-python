import math
n=int(input())
x=list(map(int,input().split()))
p=x[0]
for i in range(1,len(x)):
    p=math.lcm(p,x[i])
print(p)