n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
cnt=0
max_size = 0
# n-i>=3 일 경우에 3단짜리 탐색 시작

for i in range(n):
    for j in range(n-2):
        for k in range(3):
            if arr[i][k]==1:
                cnt+=1
            if max_size<cnt:
                max_size=cnt
                cnt=0

print(max_size)