n = int(input())
arr = list(map(int,input()))

max_cnt = 0
cnt = 0
x1,x2 = 0,0
max_dis = 0

if arr[-1]==0:
    arr.append(1)
    n+=1

for i in range(n):
    for j in range(i+1,n):
        if arr[i]==1 and arr[j]==1:
            if max_dis<j-i:
                max_dis = j-i
                x1,x2 = i,j
            i=j

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