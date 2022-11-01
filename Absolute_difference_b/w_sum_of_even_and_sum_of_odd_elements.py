n=int(input())
x=list(map(int,input().split()))
even=[]
odd=[]
for i in x:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
a=sum(even)
b=sum(odd)
if a>=b:
    print(a-b)
else:
    print(b-a)

