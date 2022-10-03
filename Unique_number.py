def fun(d,num): # (8,0) #(2,8)
    while num:
        k=num%10 #0 #8%10=8
        num=num//10 #0 # 0
        if d==k:#8==0 #2==
            return True
    return False




n=int(input())#28
s=0
while n:
    d=n%10 # 8 # 2
    n=n//10 # 2 #0
    if fun(d,s):# (8,0) #(2,8)
        print("Not Unique Number")
        break
    s=s*10+d # 8
else:
    print("Unique Number")
