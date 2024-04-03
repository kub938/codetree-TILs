def bubble_sort(n,arr):
    sorted_arr = False
    while sorted_arr==False:
        sorted_arr = True
        for i in range(n-1):
            if arr[i]>arr[i+1]:
                sorted_arr=False
                arr[i],arr[i+1] = arr[i+1],arr[i]    
    return arr

n = int(input())
arr = list(map(int,input().split()))

print(*bubble_sort(n,arr))