# 구역 1,2,3,4 = 
# 1. 좌표값이 x>x축(y값)and y>y축(x값)
# 2. 좌표값이 x>x축 and y<y축
# 3. x<x축 and y>y축
# 4. x<x축 and y<y축



n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
max_points = []

for i in range(101):
    for j in range(101):
        cnt1,cnt2,cnt3,cnt4 = 0,0,0,0
        for x,y in arr:
            if i%2==0 and j%2==0:
                if x>i and y>j:
                    cnt1+=1
                elif x>i and y<j:
                    cnt2+=1
                elif x<i and y>j:
                    cnt3+=1
                elif x<i and y<j:
                    cnt4+=1
        max_points.append(max(cnt1,cnt2,cnt3,cnt4))
max_points = [i for i in max_points if i!=0]
print(min(max_points))