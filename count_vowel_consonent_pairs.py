a=input()
i=0
j=len(a)-1
l=[]
s1='aeiouAEIOU'
s2='BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
while i<j:
    if (a[i] in s1 and a[j] in s2) or (a[j] in s1 and a[i] in s2):
        l.append((a[i],a[j]))
    i+=1
    j-=1
print(len(l))