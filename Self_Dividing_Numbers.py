def seldivnum(num):
    temp=num
    while temp>0:
        d=temp%10
        temp=temp//10
        if d==0 or num%d!=0:
            return False
    return True



a=int(input())
b=int(input())
for i in range(a,b+1):
    if seldivnum(i):
        print(i,end=" ")
