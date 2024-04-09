def heapify(arr,n,i):
    l = i*2
    r = i*2+1
    largest = i
    
    if l<=n and arr[largest] < arr[l]:
        largest = l
    
    if r<=n and arr[largest] < arr[r]:
        largest = r

    if largest!=i:
        arr[i],arr[largest] = arr[largest], arr[i]
        heapify(arr,n,largest)


def heap_sort(arr,n):
    for i in range(n//2,0,-1):
        heapify(arr,n,i)
    
    for i in range(n,0,-1):
        arr[1],arr[i] = arr[i],arr[1]
        heapify(arr,i-1,1)

n = int(input())
arr = list(map(int,input().split()))
arr.insert(0,0)

heap_sort(arr,n)

for i in range(1,n+1):
    print(arr[i], end=" ")