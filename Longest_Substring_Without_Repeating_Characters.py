def unique(n):
    l1=[]
    for  i in n:
        i=i.lower()
        if i not in l1:
            l1.append(i)
    if len(l1)==len(n):
        return True
    return False
n=input()
c=[]
l=0
for i in range(len(n)):
    for j in range(i,len(n)):
        d=n[i:j+1]
        if len(d)>2:
            if unique(d):
                if len(d)>l:
                    l=len(d)
                    z=d
if l==0:
    print('-1')
else:
    print(''.join(z))