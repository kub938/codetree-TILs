n = list(input())

dec_num = 0

if '0' not in n:
    n[-1]=0
else:
    for i in range(len(n)):
        if n[i]=='0':
            n[i]='1'
            break
n = ''.join(n)

print(int(n,2))