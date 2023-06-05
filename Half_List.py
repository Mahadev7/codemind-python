n=int(input())
x=list(map(int,input().split()))
c=n//2
l1=[]
l2=[]
for i in range(c):
    l1.append(x[i])
for i in range(c,n):
    l2.append(x[i])
l3 = l2[::-1]
print(*(l3+l1))