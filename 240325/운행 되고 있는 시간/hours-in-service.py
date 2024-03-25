n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
max_time = 0

for i in range(n):
    time = [0]*10
    for j in range(n):
        cnt=0
        if i==j:
            continue
        else:
            a,b = arr[j][0],arr[j][1]
        for l in range(a,b):
            time[l-1]+=1
    for elem in time:
        if elem>0:
            cnt+=1
    max_time=max(max_time,cnt)
            


            

    



print(max_time)