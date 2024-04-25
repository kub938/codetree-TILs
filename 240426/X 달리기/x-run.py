goal = int(input())


time = 0
run = 0
s = 0

while run != goal :
    if goal-(run+s+1)<=s:
        s-=1
    else:
        s+=1
    if s<1:
        s=1
    run+=s
    time+=1

print(time)