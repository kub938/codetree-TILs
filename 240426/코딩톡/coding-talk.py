n,m,p = map(int,input().split())

arr = [tuple(input().split()) for _ in range(m)]

people = [chr(65+i) for i in range(n)]

pos = 0
# 초기셋팅 : 첫번째 1이상값이 나오면 
for i in range(m):
    if arr[i][1]!='0':
        for j in range(i,m):
            if arr[j][0] in people:
                people.pop(people.index(arr[j][0]))
        pos = i
        break

tmp = []
for i in range(pos,p-1):
    if arr[i][1]!=arr[i-1][1]:  #값이 증가하면 안읽은 사람이 한사람 늘어난 것이므로 이전에 답장했던 사람을 추가
        if tmp:
            for e in tmp:
                people.append(e)
        else:
            people.append(arr[i-1][0])
        people.append(arr[i][0])
        
    else:
        tmp.append(arr[i][0])

for i in range(p,m):
    for j in range(i,m):
        if arr[j][0] in people:
            people.pop(people.index(arr[j][0]))


people.sort()
people = set(people)

if arr[p-1][1]!='0':
    print(*people)