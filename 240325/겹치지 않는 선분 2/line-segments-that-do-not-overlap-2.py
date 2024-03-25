n= int(input())
x_value = [tuple(map(int,input().split())) for _ in range(n)]

cnt = 0

for i in range(len(x_value)):
    for j in range(i+1,len(x_value)):
        x1,x2 = x_value[i]
        x3,x4 = x_value[j]
        if x1<x3<x2 and x1<x4<x2 or x3<x1<x4 and x3<x2<x4:
            del x_value[j]
            del x_value[i]

print(len(x_value))


        # if arr[x:x2] in 0: