a=input()
b=int(a)
c=a[::-1]
x=b*b
y=int(c)*int(c)
if str(x)==str(y)[::-1]:
    print("True")
else:
    print("False")