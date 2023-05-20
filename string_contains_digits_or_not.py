n=int(input())
for i in range(n):
    s=input()
    a=[]
    for i in s:
        if i.isdigit():
            a.append(i)
    l=len(a)
    if (l==0):
        print("No")
    else:
        print("Yes")