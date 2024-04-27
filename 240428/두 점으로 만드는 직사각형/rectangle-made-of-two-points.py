# 가장큰 오른쪽 상단 x값
# 가장작은 왼쪽 하단 y값
x1,y1,x2,y2= map(int,input().split())
a1,b1,a2,b2= map(int,input().split())

#오른쪽 하단 = min
x,y = min(x1,a1),min(y1,b1)
x2,y2 = max(x2,a2),max(y2,b2)

w = (x2-x)*(y2-y)

print(w)