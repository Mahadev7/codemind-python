n=int(input())
x=list(map(int,input().split()))
sum=0
avg=0
for i in range(len(x)):
    sum+=x[i]
    avg=sum//n
if avg in x:
    print("True")
else:
    print("False")