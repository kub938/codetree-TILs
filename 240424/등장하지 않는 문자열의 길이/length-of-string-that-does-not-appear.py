n = int(input())
s = input()
part_s = []
ans = 0
check = False
c=0
one_type = True
for i in range(2,n):
    part_s = s[c:i]
    if s.count(part_s)==1 and check:
        if one_type:
            ans = i+1-c
        else:
            ans = i-c
        break
    if s.count(part_s)>1:
        check = True
        continue
    if not check and s.count(part_s)==1:
        c=i-1
        one_type = False
   

print(ans)