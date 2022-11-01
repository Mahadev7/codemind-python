n=int(input())
list=map(int,input().split())
odd=[]
for i in list:
    if i%2!=0:
        odd.append(i)
print(sum(odd))