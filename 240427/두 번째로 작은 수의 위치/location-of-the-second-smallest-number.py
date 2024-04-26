import sys

n = int(input())
arr = list(map(int,input().split()))

if n==arr.count(arr[0]):
    print(-1)
    sys.exit()

tmp = sorted(arr[:])

tmp = list(set(tmp))
target = tmp[1]

check = True
if arr.count(target)>1:     #2개 이상이면 flase
    check = False

if check:
    ans = arr.index(target)+1
else:
    ans = -1
print(ans)