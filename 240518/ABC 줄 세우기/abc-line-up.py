n = int(input())
a = list(input().split())
sort_a = sorted(a)

cnt = 0
for i in range(n-1):
    for j in range(i+1,n):
        if sort_a[i]==a[j]:
            print(a,'before')
            a.insert(i,a.pop(j))
            cnt+=j-i
print(cnt)