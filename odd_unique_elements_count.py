n=int(input())
x=list(map(int,input().split()))
c=0
y=set(x)
for i in y:
    if i%2!=0:
        c+=1
print(c)