m1,d1,m2,d2 = map(int,input().split())
day = input()

month = [0,31,29,31,30,31,30,31,31,30,31,30,31]
days = {'Mon':0,'Tue':1,'Wed':2,'Thu':3,'Fri':4,'Sat':5,'Sun':6}

sum_month = 0
for i in range(m1,m2):
    sum_month+=month[i]

if m1==m2:
    cal_day = d2-d1
else:
    cal_day = sum_month-d1+d2

ans = cal_day//7
if days[day]<=cal_day%7:
    ans+=1

print(ans)