n,k = map(int,input().split())
arr = list(map(int,input().split()))

m_value = max(arr)
cnt = 0
ans = 0


for max_value in range(m_value,0,-1):
    if m_value==arr[0] or m_value==arr[-1]:
        ans = m_value
        break
    if cnt==k:
        break
    for j in range(n):
        if cnt==k:
            ans = max_value+1
            break
        if arr[j]>max_value:
            cnt+=1
        else:
            cnt=0


print(ans)