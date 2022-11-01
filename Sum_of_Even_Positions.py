n=int(input())
x=list(map(int,input().split()))
even=[]
for i in range(len(x)):
    if i%2==0:
        even.append(x[i])
print(sum(even))