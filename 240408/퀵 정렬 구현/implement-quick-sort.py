def quick_sort(arr):
    if len(arr)<=1:
        return arr
    
    pivot = arr[len(arr)//2]
    left,center,right = [],[],[]

    for e in arr:
        if e<pivot:
            left.append(e)
        elif e==pivot:
            center.append(e)
        else:
            right.append(e)

    return quick_sort(left) + center + quick_sort(right)

n = int(input())
arr = list(map(int,input().split()))

print(*quick_sort(arr))