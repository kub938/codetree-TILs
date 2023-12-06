arr = [list(map(int,input().split()))for _ in range(2)]

def width(arr):
    width_avg = []
    for i in arr:
        width_avg.append(sum(i)/(len(i)))
    return width_avg

def height(arr):
    height_avg = []
    h_sum=0
    for i in range(4):
        for j in range(2):
            h_sum+=arr[j][i]
        height_avg.append(h_sum/2)
        h_sum=0
    return height_avg

def all_avg(arr):
    a_avg = 0
    for i in arr:
        a_avg+=sum(i)
    return a_avg/8
        

    

print(*width(arr))
print(*height(arr))
print(all_avg(arr))