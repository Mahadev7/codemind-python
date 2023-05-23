n=int(input())
x=list(map(int,input().split()))
c=[]
s=0
for i in x:
    if i%2!=0:
        break
    c.append(i)
for  i in c:
    s+=i
print(s)