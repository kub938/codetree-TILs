n = int(input())
arr = list(map(int,input()))

x1,x2 = 0,0
max_dis = 0
ans=0
dis1= 0
dis2= 0

for i in range(n-1):
    for j in range(i+1,n):
        if arr[i]==1 and arr[j]==1:
            if max_dis<j-i:
                max_dis = j-i
            x1,x2 = i,j
            i=j

if max_dis%2==0:
    dis1 = max_dis//2
else:
    dis1 = max_dis//2+1

ans = dis1

if arr[-1]==0:
    dis2 = n-1-x2

if dis1<dis2:
    ans = dis2
print(ans)