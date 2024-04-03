def select_sort(n,arr):
    for i in range(n):
        min_val = i
        for j in range(i+1,n):
            if arr[min_val]>arr[j]:
                min_val = j
        arr[i],arr[min_val] = arr[min_val],arr[i]
    
    return arr

n=int(input())
arr = list(map(int,input().split()))

print(*select_sort(n,arr))