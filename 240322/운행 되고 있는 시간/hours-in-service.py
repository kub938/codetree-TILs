n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
max_time = 0

for i in range(n):
    time = [0]*1001
    for j in range(i,n):
        if i==j:
            continue
        else:
            cnt=0
            for a,b in enumerate(arr[j]):
                for k in range(a,b):
                    time[k]+=1
            for elem in time:
                if elem>0:
                    cnt+=1
            max_time=max(max_time,cnt)
            


            

    



print(max_time)