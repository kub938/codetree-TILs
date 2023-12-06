n = int(input())
arr = [[0 for _ in range(n)]for _ in range(n)]
cnt = 1
for i in range(n):
    for j in range(n):
        arr[j][i] = cnt 
        cnt+=1

for k in range(n):
    for t in range(n):
        print(arr[k][t],end=" ")
    print()