arr = [list(input().split()) for _ in range(5)]

for i in arr:
    for j in range(len(i)):
        print(i[j].upper(),end=" ")
    print()