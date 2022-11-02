n=int(input())
x=list(map(int,input().split()))
for i in range(len(x)):#Index Based
    if x[i]%2==0:
        a=i
print(a)