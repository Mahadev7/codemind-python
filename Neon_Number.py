a=int(input())
n=a*a
sum=0
while n>0:
    p=n%10
    sum=sum+p
    n=n//10
if sum==a:
    print("Neon Number")
else:
    print("Not Neon Number")
