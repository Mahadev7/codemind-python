n=int(input())
x=list(map(int,input().split()))
c,c1=0,0
for i in range(len(x)):
    if x[i]%2==0:
        c+=1
    else:
        c1+=1
print(c,c1)