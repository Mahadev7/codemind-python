import math
def isperfect(n):
    p=n*n
    r=math.sqrt(n)
    if int(r+0.5)**2==n:
        return True
    else:
        return False
n=int(input())
x=list(map(int,input().split()))
s=0
for i in x:
    if isperfect(i):
        s+=i
print(s)