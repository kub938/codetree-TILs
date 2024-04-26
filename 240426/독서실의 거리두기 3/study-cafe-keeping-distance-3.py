n = int(input())
arr = list(map(int,input()))

max_dis = 0
x1,x2 = 0,0
for i in range(n):
    for j in range(i+1,n):
        if arr[i]==1 and arr[j]==1:
            if max_dis<j-i:
                max_dis = j-i
                x1,x2 = i,j
            i=j



arr[(x2-x1)//2+x1]=1
min_dis = 10000
for i in range(n):
    for j in range(i+1,n):
        if arr[i]==1 and arr[j]==1:
            min_dis = min(min_dis,j-i)

print(min_dis)