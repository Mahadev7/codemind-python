n=int(input())
x=list(map(int,input().split()))
b=[]
for i in x:
    p=i*i
    b.append(p)
a=sorted(b)
for i in a:
    print(i,end=' ')