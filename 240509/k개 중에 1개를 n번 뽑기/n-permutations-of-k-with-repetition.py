k,n = map(int,input().split())

arr = []
def min_num(n):
    if n==0:
        print(*arr)
        return
    for i in range(1,1+k):
        arr.append(i)
        min_num(n-1)
        arr.pop()

min_num(n)