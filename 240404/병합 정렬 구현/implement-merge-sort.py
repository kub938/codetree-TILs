# 변수 선언 및 입력
n = int(input())
arr = list(map(int, input().split()))
merge_arr = [0] * n 

def merge(low, mid, high):
    i, j = low, mid + 1                 # 각 리스트 내의 원소 위치를 잡습니다.
    
    k = low            
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            merge_arr[k]=arr[i]
            i+=1
            k+=1

        else:
            merge_arr[k] = arr[j]
            j+=1
            k+=1

    while i<=mid:
        merge_arr[k]=arr[i]
        k+=1
        i+=1

    while j<=high:
        merge_arr[k]=arr[j]
        k+=1
        j+=1
    
    for k in range(low, high+1):
        arr[k] = merge_arr[k]
    


def merge_sort(low,high):
    if low<high:
        mid = (low+high)//2
        merge_sort(low,mid)
        merge_sort(mid+1,high)
        merge(low,mid,high)

merge_sort(0,n-1)

for elem in arr:
    print(elem,end=" ")