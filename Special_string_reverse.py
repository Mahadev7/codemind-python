a=input()
x=list(a)
i=0
j=len(x)-1
while i<j:
    if x[i].isalpha() and x[j].isalpha():
        x[i],x[j]=x[j],x[i]
        i+=1
        j-=1
    elif x[i].isalpha() and not x[j].isalpha():
        j-=1
    elif not x[i].isalpha() and x[j].isalpha():
        i+=1
    else:
        i+=1
        j-=1    
c=''.join(x)
print(c)