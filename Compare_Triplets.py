x=list(map(int,input().split()))
y=list(map(int,input().split()))
c,p=0,0
for i in range(len(x)):
    if x[i]>y[i]:
        c+=1
    elif x[i] < y[i] :
        p+=1
print(c,p)