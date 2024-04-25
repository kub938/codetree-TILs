import sys

n,m,p = map(int,input().split())
arr = [tuple(input().split()) for _ in range(m)]
target_v = int(arr[p-1][1])
target_a = arr[p-1][0]

if target_v==0:
    sys.exit()

for i in range(n):
    person = chr(65+i)
    read = False
    for c,u in arr:
        u = int(u)
        if u>=target_v and c==person:
            read = True
    if not read:
        print(person,end=" ")



## 망한코드
# 초기 idea = people 배열 셋팅후 target의 아래에 있는것만 빼면 정답이 나옴
# -> 실패 : 위에서 같은 읽은횟수가 나오면 오답, 맨 위에 0이 있으면 답은 ""이 나옴
# -> 0이상 값이 나올때 까지 for문을 돌려서 그 부분을 target으로 생각하고 끝까지 나오는 알파벳을 pop하여 초기값 설정
# -> 그후 다시 맨 위에서부터 값이 증가하면 사람이 늘어난것이므로 해당하는 알파벳 추가, 같은 숫자일 경우 tmp에 넣었다가 값이 올라가면 한꺼번에 추가
# -> 실패 : 같은 알파벳이 나오면 
# ->