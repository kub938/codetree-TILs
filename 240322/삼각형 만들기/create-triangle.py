import sys

n = int(input())
arr_x,arr_y = [],[]
max_area = -sys.maxsize
for i in range(n):
    x,y = map(int,input().split())
    arr_x.append(x)
    arr_y.append(y)

def check_xy(x,y):
    check_x = False
    check_y = False
    for i in range(3):
        for j in range(i,3):
            if x[i]==x[j]:
                check_x = True
            if y[i]==y[j]:
                check_y = True
    return check_x and check_y

def area(x,y):
    min_x,min_y = 10000,10000
    max_x,max_y = -10000,-10000

    for i in range(3):
        min_x,min_y = min(min_x,x[i]),min(min_y,y[i])
        max_x,max_y = max(max_x,x[i]),max(max_y,y[i])
    
    area = (max_x-min_x)*(max_y-min_y)
    return area

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            arr_nx,arr_ny = [],[]
            arr_nx.append(arr_x[i])
            arr_nx.append(arr_x[j])
            arr_nx.append(arr_x[k])

            arr_ny.append(arr_y[i])
            arr_ny.append(arr_y[j])
            arr_ny.append(arr_y[k])
            if not check_xy(arr_nx,arr_ny):
                continue
            else:
                max_area = max(max_area,area(arr_nx,arr_ny))

if max_area==-sys.maxsize:
    print(0)
else:
    print(max_area)