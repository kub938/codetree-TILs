n = int(input())
arr = [list(input().split()) for _ in range(n)]
stack = []
for i in range(n):
 
    if 'push' in arr[i]:
        stack.append(int(arr[i][1]))
    elif 'size' in arr[i]:
        print(len(stack))
    elif 'empty' in arr[i]:
        if len(stack)>0:
            print(0)
        else:
            print(1)
    elif 'pop' in arr[i]:
        print(stack.pop())
    else:
        print(stack[-1])