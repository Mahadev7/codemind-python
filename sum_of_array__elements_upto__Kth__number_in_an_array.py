n=int(input())
x=list(map(int,input().split()))
k=int(input())
a=[]
p=0
for i in x:
    if i==k:
        break
    a.append(i)
b= sum(a)
print(b+k)