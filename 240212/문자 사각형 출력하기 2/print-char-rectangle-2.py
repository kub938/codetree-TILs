n = int(input())
result = [[0]*n for _ in range(n)]

def change_eng(cnt):
    if cnt>90:
        cnt-=36
        return chr(cnt)
    else:
        return chr(cnt)

#A = 65
# 65~ 쭉 출력
# for col 1,n+1:
#  
#    if col%2==0 
    #     for row 1,n+1:
    #             #행-1
    # else: 
    #     for :
    #         행+1
#  열+1
cnt = 65

for col in range(n):
    if col % 2 != 0:
        for row in range(n - 1, -1, -1):
            if cnt>90:
                cnt-=36
            result[row][col] = chr(cnt)
            cnt += 1
    else:
        for row in range(n):
            if cnt>90:
                cnt-=36
            result[row][col] = chr(cnt)
            cnt += 1
    

for i in result:
    print(*i)