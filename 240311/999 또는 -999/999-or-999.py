import sys

min_value,max_value = 0,0
arr = list(map(int,input().split()))
arr_cut = arr[:2]
max_value = max(arr_cut)
min_value = min(arr_cut)
arr = arr[2:]

for elem in arr:
    if elem==999 or elem==-999:
        print(max_value,min_value)
        break
    elif elem>max_value:
        max_value=elem
    elif elem<min_value:
        min_value=elem