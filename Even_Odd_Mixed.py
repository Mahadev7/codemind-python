a=int(input())
l=len(str(a))
e=0
o=0
while a:
    p=a%10
    if p%2==0:
        e+=1
    else:
        o+=1
    a=a//10
if e==l:
    print("Even")
elif o==l:
    print("Odd")
else:
    print("Mixed")