a,b,c = map(int,input().split())

move = 0 
while b-a !=1 or c-b!=1:
    if b-a>= c-b :
        c=b-1
        b,c =c,b
        move+=1
    else:
        a = b+1
        a,b=b,a
        move+=1

print(move)