n=int(input())
x=list(map(int,input().split()))
a=[]
b=[]
c=n//2
for i in range(c):
    a.append(x[i])
for i in range(c,n):
    b.append(x[i])
b=b[::-1]
print(*(b+a))