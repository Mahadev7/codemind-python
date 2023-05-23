a=list(map(str,input().split()))
for i in a:
    i=i.lower()
    if i==i[::-1]:
        print("True")
    else:
        print("False")