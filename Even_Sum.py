n=int(input())
list=map(int,input().split())
even=[]
for i in list:
    if i%2==0:
        even.append(i)
print(sum(even))