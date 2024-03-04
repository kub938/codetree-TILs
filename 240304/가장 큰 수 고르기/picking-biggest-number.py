m = list(map(int,input().split()))
max_int = 0

for elem in m:
    if max_int<elem:
        max_int=elem

print(max_int)