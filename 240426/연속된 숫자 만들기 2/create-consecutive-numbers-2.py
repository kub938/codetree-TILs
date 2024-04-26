a,b,c = map(int,input().split())

cnt = 0
while b-a>1 or c-b>1:
    if b-a<=c-b and c-b!=1:
        c = a+(b-a)//2
        b,c = c,b
        cnt+=1
    elif b-a>c-b:
        a = b+(c-b)//2
        a,b = b,a
        cnt+=1

print(cnt)