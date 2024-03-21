import sys

arr = list(map(int,input().split()))
n = len(arr)
one = 0
two = 0
three = 0
sum_all = sum(arr)
max_sum = -sys.maxsize
min_sum = sys.maxsize
min_diff = sys.maxsize

for i in range(n):
    for j in range(n):
        for k in range(n):
            for l in range(n):
                if i!=j and i!=k and i!=l and j!=k and j!=l and k!=l:
                    one=arr[i]+arr[j]
                    two = arr[k]+arr[l]
                    three = sum_all-(one+two)
                    min_diff = min(min_diff,(max(one,two,three)-min(one,two,three)))
                else:
                    continue
print(min_diff)