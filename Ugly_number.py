def uglynum(n):
    if n==0:
        return False
    for i in [2,3,5]:
        while n%i==0:
            n//=i
    if n==1:
        print("Ugly Number")
    else:
        print("Not Ugly Number")
n=int(input())
uglynum(n)