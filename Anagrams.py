a=input()
b=input()
a=a.lower()
b=b.lower()
if sorted(a)==sorted(b):
    print("True")
else:
    print("False")