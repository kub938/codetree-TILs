from collections import deque


n, k = map(int,input().split())

q = deque([i for i in range(n,0,-1)])


while len(q)!=0:
    for i in range(k-1):
        tmp = q.pop()
        q.appendleft(tmp)
    print(q.pop(),end=" ")