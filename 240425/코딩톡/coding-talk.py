n,m,p = map(int,input().split())

arr = [tuple(input().split()) for _ in range(m)]

people = [chr(65+i) for i in range(n)]

for i in range(p-1,m):
    c,u = arr[i]
    if c in people:
        people.pop(people.index(c))



if p>1 and arr[p-2][1]==arr[p-1][1]:
    if arr[p-2][0] in people:
        people.pop(people.index(arr[p-2][0]))
        print(*people)
elif arr[p-1][1]!='0':
    print(*people)