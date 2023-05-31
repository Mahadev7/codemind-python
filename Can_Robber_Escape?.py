a=int(input())
x=list(map(int,input().split()))
c=0
for i in range(len(x)):
    if x[i]%2==1:
        c+=1
if c>2:
    print("NO")
else:
    print("YES")