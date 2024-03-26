n = int(input())
arr = []
for i in range(n):
    s = input().split()
    if s[0]=='push_back':
        k=int(s[1])
        arr.append(k)
    elif s[0]=='pop_back':
        arr.pop()
    elif s[0]=='size':
        print(len(arr))
    elif s[0]=='get':
        k=int(s[1])
        print(arr[k-1])