n = int(input())
s = input()
part_s = []
ans = 0

for i in range(1,n):
    part_s = s[:i]
    if s.count(part_s)>1:
        continue
    else:
        ans=i
        break

print(ans)