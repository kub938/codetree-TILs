a,b,x,y = map(int,input().split())

move = 0

print(min(abs(a-b),abs(a-x)+abs(y-b),abs(a-y)+abs(x-b)))


#a-b
#a-x + y-b
#a-y + y-b