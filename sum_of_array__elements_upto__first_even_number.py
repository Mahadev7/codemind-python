n=int(input())
x=list(map(int,input().split()))
a=[]
p=0
for i in x:
    if i%2==0:
        break
    a.append(i)
for i in a:
   p+=i
print(p)