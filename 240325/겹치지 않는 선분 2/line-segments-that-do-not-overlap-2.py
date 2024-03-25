n= int(input())
x = [tuple(map(int,input().split())) for _ in range(n)]

ans = 0

for i in range(n):
    overlap = False

    for j in range(n):
        if j == i :
            continue

        x1,x2 = x[i]
        x3,x4 = x[j]
        
        if (x[i][0] <= x[j][0] and x[i][1] >= x[j][1]) or (x[i][0] >= x[j][0] and x[i][1] <= x[j][1]):
            overlap = True
            break

    if overlap == False:
        ans +=1

print(ans)


        # if arr[x:x2] in 0: