n = int(input())
students = [list(map(int,input().split())) for _ in range(n)]

students.sort(key=lambda x: (x[0],-x[1]))

for i in range(n):
    print(*students[i],i+1)