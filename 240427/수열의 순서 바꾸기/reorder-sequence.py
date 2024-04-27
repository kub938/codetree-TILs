n = int(input())
arr = list(map(int,input().split()))
sorted_arr = sorted(arr)

# 젤 작은값은 젤 큰값 뒤로
# 젤 큰값은 del 하고 sorted_arr.pop()
# 중간 값은 젤 작은값 뒤로

ans = 0
while 1:
    if sorted_arr == arr:
        break
    while arr[-1]==sorted_arr[-1]:
        arr.pop()
        sorted_arr.pop()
    max_n = max(arr)
    min_n = min(arr)
    if arr[0]==max_n:
        del arr[0]
        sorted_arr.pop()
    elif arr[0]==min_n:
        max_idx = arr.index(max_n)
        arr.insert(max_idx+1,arr[0])
        del arr[0]
    else:
        min_idx = arr.index(min_n)
        arr.insert(min_idx+1,arr[0])
        del arr[0]

    ans+=1


print(ans)