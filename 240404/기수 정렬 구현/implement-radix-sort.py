def radix_sort(n,arr):
    new_arr = [[] for _ in range(10)]
    for i in range(len(str(arr[0]))):
        for j in range(n):
            s = str(arr[j])
            new_arr[int(s[-i-1])].append(arr[j])
        
        for j in range(10):
            store_arr=[]
            for k in new_arr:
                if k==[]:
                    continue
                else:
                    store_arr.append(*k)
        arr=store_arr
    
    return arr

n = int(input())
arr = list(map(int,input().split()))


ans = radix_sort(n,arr)

for elem in ans:
    print(elem,end=" ")