a,b = map(int,input().split())
n = int(input(),a)

if b==8:
    n = oct(n)
elif b==2:
    n = bin(n)
elif a==16:
    n = hex(n)

print(str(n)[2:])