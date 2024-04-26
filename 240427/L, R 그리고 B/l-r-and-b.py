arr = [list(input()) for _ in range(10)]

b_x,b_y = 0,0
l_x,l_y = 0,0

for i in range(10):
    if 'B' in arr[i]:
        b_x= arr[i].index('B')
        b_y=i
    if 'L' in arr[i]:
        l_x = arr[i].index('L')
        l_y=i
    if 'R' in arr[i]:
        r_x = arr[i].index('R')
        r_y = i


s_dis = abs(b_y-l_y) + abs(b_x-l_x)-1 

if r_x == l_x == b_x and (l_y<r_y<b_y or b_y<r_y<l_y) or (r_y == l_y == b_y):    
    s_dis+=2


print(s_dis)