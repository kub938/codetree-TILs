n = int(input())
line = [0]*501
point = []
for i in range(n):
    a,b = map(int,input().split())
    a = a+1
    if a>b:
        a,b = b,a
        for j in range(a,b):
            line[j]+=1
    elif a==b:
        point.append(a)
    else:
        for j in range(a,b):
            line[j]+=1

if point:
    for i in point:
        if line[i-1]==0 or line[i+1]==0:
            continue
        else:
            line[i]+=1
print(max(line)-1)