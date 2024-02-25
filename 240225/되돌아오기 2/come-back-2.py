coms = input()

dxs,dys = [-1,0,1,0],[0,1,0,-1]
dx,dy = 0,0
dir_num =0
cnt = 0
check = 0

for com in coms:
    cnt+=1
    if com=='L':
        dir_num=(dir_num+1)%4
    elif com=='R':
        dir_num=(dir_num+3)%4
    else:
        dx,dy = dx+dxs[dir_num],dy+dys[dir_num]
    
    if dx==0 and dy==0:
        check=-1
        print(cnt)
        break

if check ==0:
    print(-1)