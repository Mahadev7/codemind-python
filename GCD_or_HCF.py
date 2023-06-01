a,b=map(int,input().split())
x,y=[],[]
c=[]
for i in range(1,a+1):
    if a%i==0:
        # print(i)
        x.append(i)
for i in range(1,b+1):
    if b%i==0:
        y.append(i)
for i in x:
    if  i in y:
        c.append(i)
print(max(c))