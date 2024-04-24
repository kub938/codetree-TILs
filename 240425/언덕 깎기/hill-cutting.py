n = int(input())
arr = [int(input()) for _ in range(n)]

price=0

for i in range(n):
    best = 0
    for j in range(n):
        high = max(arr)
        if high-17 >= arr[j]:
            best = max(arr[j],best)
    if best:
        level = high-17-best
        price += level**2
        arr[arr.index(high)]= high -level
        arr[arr.index(best)] = best+level


print(price)