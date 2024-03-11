n = int(input())
arr = map(int,input().split())
ans = [0]*1001

for elem in arr:
    ans[elem]+=1

for i in range(1000,-1,-1):
    if not 1 in ans:
        print(-1)
        break
    if ans[i]==1:
        print(i)
        break