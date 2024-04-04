def radix_sort(n,arr):
    for i in range(len(arr[0])):
        new_arr = [[] for _ in range(10)]

        for j in range(n):
            s = str(arr[j])
            new_arr[int(s[-i-1])].append(arr[j])           
        
        
          
        store_arr=[] 
        for k in new_arr:
            if k==[]:
                continue
            else:
                for l in k:
                    store_arr.append(l)
        arr=store_arr
    return arr

n = int(input())
arr = list(input().split())

max_len = 0 
for i in arr:
    max_len = max(max_len,len(i))

for i in range(len(arr)):
    arr[i] = arr[i].zfill(max_len)

ans = radix_sort(n,arr)

for elem in ans:
    elem = elem.lstrip('0')
    print(elem,end=" ")


# 가장큰값 찾아서 길이 잰다음 zfill로 다른애들도 0 으로 채워넣어