def get_pfs(num):# num = 0
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    return sum
x=int(input())
y=int(input())
if get_pfs(x)==y and get_pfs(y)==x:
    print("Amicable")
else:
    print("Not Amicable")

