n=int(input())
temp=n
rev=0
n=abs(n)
while n>0:
    p=n%10
    rev=(rev*10)+p
    n=n//10
if temp<0:
    print('-%d'%rev)
else:
    print(rev)