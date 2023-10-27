for _ in range(int(input())):
    a = input()
    if a == a[::-1] and len(a)%2==0:
        print("YES " "EVEN")
    elif a == a[::-1] and len(a)%2!=0:
        print("YES " "ODD")
    else:
        print("NO")