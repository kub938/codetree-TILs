n = int(input())
arr = list(map(int,input()))

max_cnt = 0
cnt = 0
x1,x2 = 0,0
max_dis = 0

last_zero = False
for i in range(1):
    for j in range(i+1,n):
        if arr[i]==1 and j==n-1 and arr[-1]==0 and j-i>max_dis:
            max_dis=j-i
            last_zero=True
        elif arr[i]==1 and (arr[j]==1 or j==n-1):
            if max_dis<j-i:
                max_dis = j-i
                x1,x2 = i,j
            i=j
            

if last_zero:
    arr[-1]=1
else:
    arr[(x1+x2)//2+x1] = 1

for i in range(1):
    if arr[i]==1:
        for j in range(i+1,n):
            if arr[j]==1:
                if max_dis<j-i:
                    max_dis = j-i
                    x1,x2 = i,j
                i=j
            elif j==n-1 and arr[-1]==0 and j-i>max_dis:
                print(j-i,j,i)
                max_dis=j-i
                last_zero=True
            

if last_zero:
    arr[-1]=1
else:
    arr[(x1+x2)//2+x1] = 1



min_dis = 1001
for i in range(n):
    for j in range(i+1,n):
        if arr[i]==1 and arr[j]==1:
            if min_dis>j-i:
                min_dis = j-i
                x1,x2 = i,j
            i=j

print(min_dis)