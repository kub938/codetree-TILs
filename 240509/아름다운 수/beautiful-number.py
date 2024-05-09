n = int(input())
beautiful_n = []
arr = []
ans = 0

def b_num(n):
    global ans
    if n==0:
        if check(arr):
            ans+=1
        return
    for i in range(1,5):
        arr.append(i)
        b_num(n-1)
        arr.pop()

def check(arr):
    i =0
    while i<n:
        target = arr[i]
        for j in range(i,target+i):
            if n<=j or arr[j]!=target:
                return False
        i+=target
    return True    

b_num(n)

print(ans)