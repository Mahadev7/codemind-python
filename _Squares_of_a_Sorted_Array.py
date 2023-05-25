n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    p=i*i
    b.append(p)
x=sorted(b)
print(*x)