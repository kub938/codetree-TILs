x1,y1,x2,y2 = map(int,input().split())
a1,b1,a2,b2 = map(int,input().split())

x,y = min(x1,a1),min(y1,b1)
c,d = max(x2,a2),max(y2,b2)

w = max(c-x,d-y)
print(w**2)