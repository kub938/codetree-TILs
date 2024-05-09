n = int(input())
line = [0]*101

for i in range(n):
    a,b = map(int,input().split())
    if a>b:
        a,b = b,a
    for j in range(a,b+1):
        line[j]+=1

print(max(line)-1)