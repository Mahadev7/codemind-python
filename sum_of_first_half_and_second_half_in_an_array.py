n=int(input())
x=list(map(int,input().split()))
c=n//2
s=0
p=0
for i in range(c):
    s+=x[i]
print(s)
for i in range(c,n):
    p+=x[i]
print(p)