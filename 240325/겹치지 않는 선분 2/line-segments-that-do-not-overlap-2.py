n= int(input())
x_value = [tuple(map(int,input().split())) for _ in range(n)]

ans = 0

for i in range(n):
    overlap = False
    for j in range(n):
        if j == i :
            continue

        x1,x2 = x_value[i]
        x3,x4 = x_value[j]
        
        if x1<=x3<=x2 and x1<=x4<=x2 or x3<=x1<=x4 and x3<=x2<=x4:
            overlap = True
            break
            
    if overlap == False:
        ans +=1

print(ans)


        # if arr[x:x2] in 0: