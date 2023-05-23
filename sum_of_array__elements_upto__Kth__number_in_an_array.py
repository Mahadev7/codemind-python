n=int(input())
x=list(map(int,input().split()))
k=int(input())
a=[]
for i in x:
    if i==k:
        break
    a.append(i)
print(sum(a)+k)