def isHappy(n): #32
    r = s = 0;    
    while(n > 0):    
        r = n%10   #32%10=2,3%10=3 ,13%10=3,1%10=1,10%10=0  1%10=1 
        s += r**2  #0+4=4,4+9=13 ,0+9,9+(1**2)=10,0+0**2=0  0+1 
        n //= 10    #3 #1 #10//10=1 1//10=0
    return s  #13 #10 #1
        
n = int(input())    #32
res=n;    #32
     
while(res != 1 and res != 4):    
    res = isHappy(res)#FC    
     
if(res == 1):    
    print("True");    
elif(res == 4):    
    print("False");   