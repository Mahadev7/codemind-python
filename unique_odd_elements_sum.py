n=int(input())
x=list(map(int,input().split()))
s=0
y=set(x)
for i in y:
    if i%2!=0:
        s+=i
print(s)