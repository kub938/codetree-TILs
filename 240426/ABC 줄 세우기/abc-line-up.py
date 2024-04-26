n = int(input())
arr = list(input().split())

sorted_arr = [chr(65+i) for i in range(n)]


move = 0
i = 0
while arr != sorted_arr:
    if arr[i]!= sorted_arr[i]:
        x = arr.index(sorted_arr[i])
        move += x-i
        a = arr.pop(x)
        arr.insert(i,a)
    i+=1
        


        
    


print(move)