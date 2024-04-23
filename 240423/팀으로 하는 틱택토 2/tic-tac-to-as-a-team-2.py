arr = [list(input()) for _ in range(3)]


cnt=0
cross1,cross2 = [],[]
for i in range(3):
    col = []
    for j in range(3):
        col.append(arr[j][i])
        if j==i:
            cross1.append(arr[i][j])
            cross2.append(arr[-i-1][j])
    if arr[i].count(arr[i][0])==2 or arr[i].count(arr[i][1])==2 :
        cnt+=1
    if col.count(col[0])==2 or col.count(col[1])==2:
        cnt+=1
  
if cross1.count(cross1[0])==2 or cross1.count(cross1[1])==2:
    cnt+=1
if cross2.count(cross2[0])==2 or cross2.count(cross2[1])==2:
    cnt+=1

print(cnt)