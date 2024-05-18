n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

students = []
for i in range(n):
    students.append([*arr[i],i+1])

students.sort(key=lambda x: (x[0],-x[1]))

for i in range(n):
    print(*students[i])