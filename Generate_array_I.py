n=int(input())
a=list(map(int,input().split()))
z=[]
for i in range(0,n,2):
    x=a[i]
    y=a[i+1]
    for i in range(y):
        z.append(x)
for i in z:
    print(i,end=' ')