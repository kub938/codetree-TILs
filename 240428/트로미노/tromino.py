n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]


def in_range(c,r):
    return 0<=c<m and 0<=r<n

def L_block():
    max_value = 0
    if in_range(c+1,r-1): #L
        max_value = max(max_value,arr[r][c]+arr[r][c+1]+arr[r-1][c])
    if in_range(c+1,r+1): 
        max_value = max(max_value,arr[r][c]+arr[r+1][c]+arr[r][c+1])
    if in_range(c-1,r+1): 
        max_value = max(max_value,arr[r][c]+arr[r+1][c]+arr[r][c-1])
    if in_range(c-1,r-1): 
        max_value = max(max_value,arr[r][c]+arr[r-1][c]+arr[r][c-1])
    return max_value

def m_block():
    max_value = 0
    if in_range(c+2,r):
        max_value = max(sum(arr[r][c:c+2]),max_value)
    elif in_range(c,r+2):
        max_value = max(max_value,arr[r][c]+arr[r+1][c]+arr[r+2][c])
    return max_value

ans = 0
for r in range(n):
    for c in range(m):
        ans = max(ans,m_block(),L_block())


print(ans)