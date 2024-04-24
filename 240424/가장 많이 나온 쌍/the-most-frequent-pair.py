n, m = map(int,input().split())

arr = [list(map(int,input().split())) for i in i if i[::-1] not in arr]