a=input()
d={}
for i in a:
    # 1 1 2 3 
    i=int(i)
    if i not in d:
        d[i]=1 # '1':1
    else:
        d[i]+=1
s1,s2=0,0
for i,j in d.items():
    s1+=1
    if j==1:
        s2+=1
if s1==s2:
    print("Unique Number")
else:
    print("Not Unique Number")
        