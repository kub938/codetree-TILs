arr = [list(input()) for _ in range(10)]

b_x,b_y = 0,0
l_x,l_y = 0,0

for i in range(10):
    if 'B' in arr[i]:
        b_x= arr[i].index('B')
        b_y=i
    elif 'L' in arr[i]:
        l_x = arr[i].index('L')
        l_y=i
    elif 'R' in arr[i]:
        r_x = arr[i].index('R')
        r_y = i


s_dis = abs(b_y-l_y) + abs(b_x-l_x)-1 

if r_x == l_x == b_x:    
    s_dis+=2
print(s_dis)