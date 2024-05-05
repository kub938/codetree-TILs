n = int(input())
cnt = 0
arr = []

def is_beautiful():
    i = 0
    while i<n:
        if i+arr[i]-1>=n:
            return False

        for j in range(i,i+arr[i]):
            if arr[i]!=arr[j]:
                return False
        i+=arr[i]
    return True
            


def b_num(c):
    global cnt

    if c==n:
        if is_beautiful():
            cnt+=1
        return

    for i in range(1,5):
        arr.append(i)
        b_num(c+1)
        arr.pop()

b_num(0)
print(cnt)