a,b = map(int,input().split())
n = int(input(),a)

if b==8:
    n = str(oct(n))[2:]
elif b==2:
    n = str(bin(n))[2:]
elif a==16:
    n = str(hex(n))[2:]

print(n)