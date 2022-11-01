n=int(input())
x=list(map(int,input().split()))
odd=[]
for i in range(len(x)):
    if i%2!=0:
        odd.append(x[i])
print(sum(odd))
