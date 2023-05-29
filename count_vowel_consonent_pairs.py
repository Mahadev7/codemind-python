s=input()
a=[]
x='AEIOUaeiou'
y='BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
i=0
j=len(s)-1
while i<j:
    if (s[i] in x and s[j] in y) or (s[i] in y and s[j] in x):
        a.append((s[i],s[j]))
    i+=1
    j-=1
print(len(a))