def seldivnum(num):#15  21 22
    temp=num#1 #15  21 22
    while temp>0:#15>0 10>0  3>0  21  22
        d=temp%10#15%10=5  21%10=1  22%10=2
        temp=temp//10 #0 10//10==1 3//10==0 #15//10=1 21//10=2  22//10=2
        if d==0 or num%d!=0: #10%0!=0   3%3!=0  (5==0 or 15%5!=0)  (1==0 or 21%1!=0) (2==0 or 21%2!=0)
            return False
    return True



a=int(input())
b=int(input())
for i in range(a,b+1):#(1,5)  3
    if seldivnum(i):#1 # 10  3
        print(i,end=" ")



# In the Function defnition if "if" condition there must be satisfy atleast one condition
# Then it print "False"
#if it doesnot satisfy anyone enter into else block and return "True"
#temp=10 13 14 15 16 17 18 19 20 22 are the exists with the False statement because enters into "if" block
