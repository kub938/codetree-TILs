n,m,k = map(int,input().split())

students = [0 for _ in range(n)]

pay = -1

for i in range(m):
    num = int(input())
    students[num-1]+=1
    if students[num-1]>=k:
        pay = num
        break
        
print(pay)