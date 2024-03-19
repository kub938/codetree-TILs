# G,H가 들어있고 g와 h가 같은 갯수가 아닐때
MAX_NUM = 100

n = int(input())

arr = [0] * (MAX_NUM+1)
max_len = 0
ans = 0

for _ in range(n):
    x,c = input().split()
    x = int(x)
    
    arr[x] = 1 if c=='G' else 2

for i in range(MAX_NUM+1):
    for j in range(i,MAX_NUM+1):
        if arr[i]==0 or arr[j]==0:
            continue
        g_cnt = 0
        c_cnt = 0

        for k in range(i,j+1):
            if arr[k]==1:
                g_cnt+=1
            if arr[k]==2:
                c_cnt+=1
            
        if g_cnt==c_cnt or g_cnt==0 or c_cnt==0:
            leng = j-i
            max_len = max(max_len, leng)

print(max_len)