num=int(input())
sum=0
prod=1
while num:
    a=num%10
    sum=sum+a
    prod=prod*a
    num=num//10
if sum==prod:
    print("Spy Number")
else:
    print("Not Spy Number")