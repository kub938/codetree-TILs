n = int(input())
s = input()
part_s = []
ans = 0
check = False
c=0
for i in range(2,n):
    part_s = s[c:i]
    if s.count(part_s)==1 and check:
        if part_s.count(part_s[0])==len(part_s):
            if s[i+1]!=part_s[-1]:
                ans=i+1-c
                break
            continue
        ans = i-c
        break
    if s.count(part_s)>1:
        check = True
        continue
    if not check and s.count(part_s)==1:
        c=i-1
   

print(ans)