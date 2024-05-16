x,y = map(int,input().split())

ans = 0
for i in range(x,y+1):
    i = list(str(i))
    i = sorted(list(map(int,i)))
    target1 = i[0]
    target2 = i[-1]
    if len(i)-i.count(target1)==1 or len(i)-i.count(target2)==1:
        ans+=1
        
print(ans)