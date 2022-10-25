def Spy(num):#1124
    s=0
    p=1
    while num>0:#1124 112 11 1  0>0{fails}
        a=num%10 # 1124%10=4 2 1 1 
        s=s+a   # 0+4=4  6 7 8
        p=p*a   #1*4=4   8  8 8
        num=num//10  # 112 11  1 0
    if s==p:
        print("Spy Number")
    else:
        print("Not Spy Number")
n=int(input())
c=Spy(n)