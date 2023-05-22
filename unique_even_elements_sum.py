n=int(input())
a=list(map(int,input().split()))
s=0
a1=set(a)
for i in a1:
    if i%2==0:
        s+=i
print(s)