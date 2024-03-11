import sys

max_value = -999
min_value = 999
arr = map(int,input().split())

for elem in arr:
    if elem==999 or elem==-999:
        print(max_value,min_value)
        break
    elif elem>max_value:
        max_value=elem
    elif elem<min_value:
        min_value=elem