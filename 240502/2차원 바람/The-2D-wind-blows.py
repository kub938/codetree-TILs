import copy,sys

n,m,Q = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
q = [list(map(int,input().split())) for _ in range(Q)]

if Q==0:
    for i in arr:
        print(*i)
    sys.exit()
def spin(r1,c1,r2,c2):
    tmp = arr[r1+1][c1]
    #직사각형 왼쪽 변부터 반시계 반향으로 진행, 한칸식 당김
    for i in range(r1+1,r2):
        arr[i][c1]=arr[i+1][c1]
    for i in range(c1,c2):
        arr[r2][i]=arr[r2][i+1]
    for i in range(r2,r1-1,-1):
        arr[i][c2]=arr[i-1][c2]
    for i in range(c2,c1,-1):
        arr[r1][i]=arr[r1][i-1]
    arr[r1][c1] = tmp

def cal_avg(arr,r1,c1,r2,c2):
    for i in range(r1,r2+1):
        for j in range(c1,c2+1):
            cnt = 1
            sum_value=arr[i][j]
            if 0<=(i-1):
                sum_value+=arr[i-1][j]
                cnt+=1
            if i+1<n:
                sum_value+=arr[i+1][j]
                cnt+=1
            if 0<=(j-1):
                sum_value+=arr[i][j-1]
                cnt+=1
            if j+1<m:
                sum_value+=arr[i][j+1]
                cnt+=1
            ans[i][j]=sum_value//cnt

for e in q:
    r1,c1,r2,c2 = e
    r1,c1,r2,c2 = r1-1,c1-1,r2-1,c2-1
    spin(r1,c1,r2,c2)
    ans = copy.deepcopy(arr)
    cal_avg(arr,r1,c1,r2,c2)


for i in ans:
    print(*i)