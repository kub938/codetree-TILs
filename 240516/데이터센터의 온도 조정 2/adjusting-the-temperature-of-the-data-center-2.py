n,c,g,h = map(int,input().split())
t = [list(map(int,input().split())) for _ in range(n)] 
arr = [0]*1001


def cal_value(l,H,t):
    if t<l:
        return c
    elif t>H:
        return h
    else:
        return g

max_value = 0
for i in range(1001):
    sum_value = 0
    for l,H in t:
        sum_value+=cal_value(l,H,i)
        max_value = max(sum_value,max_value)

print(max_value)