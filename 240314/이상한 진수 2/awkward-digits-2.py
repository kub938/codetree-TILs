n = list(input())

dec_num = 0

if '0' not in n:
    for i in range(1,len(n)):
        dec_num += 2**i
    print(dec_num)
else:
    for i in range(len(n)):
        if n[i]=='0':
            n[i]='1'
            break
    for i in range(1,len(n)+1):
        if n[-i]=='1':
            dec_num+=2**(i-1)
    print(dec_num)