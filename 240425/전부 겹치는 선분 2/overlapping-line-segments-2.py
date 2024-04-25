import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력:
n = int(input())
x1_list, x2_list = [], []
for _ in range(n):
    x1, x2 = tuple(map(int, input().split()))
    x1_list.append(x1)
    x2_list.append(x2)

ans = False
   
# 모든 선분을 한번씩 지어 보고, 모든 상황에 대해
# 전부 겹치는 지점을 하나라도 만들 수 있는지 판단합니다.
for skip in range(n):
    max_x1, min_x2 = 0, INT_MAX
    possible = False
    for i in range(n):
        if i == skip: 
            continue

        # 시작점 중 가장 뒤에 있는 좌표와 끝점 중 가장 앞에 있는 점의 좌표를 확인합니다.
        max_x1 = max(max_x1, x1_list[i])
        min_x2 = min(min_x2, x2_list[i])

    # 만약 어느 한 선분이라도 시작점이 다른 선분의 끝점보다 뒤에 온다면
    # 선분이 전부 겹칠 수 없습니다.
    if min_x2 >= max_x1:
        possible = True
    else:
        possible = False
    
    # 만약 한 가지 방법이라도 전부 겹치는 지점을 만들 수 있다면,
    # 하나의 선분을 적절하게 제거했을 때 전부 겹칠수 있다는 것이 되므로 할 수 있게 됩니다.
    if possible:
        ans = True

if ans:
    print("Yes")
else:
    print("No")