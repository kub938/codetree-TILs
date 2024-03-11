n = int(input())
arr = list(map(int,input().split()))

ans,sum_lan = [],0
# for 문을 돌려서(1~n+1까지) arr[i]-i 만큼 뺀뒤 arr의 모든 elem 에 곱해서 더한다.
#완전 탐색

for i in range(n):
    for j in range(n):
        sum_lan+=arr[j]*abs(i-j)
    ans.append(sum_lan)
    sum_lan=0

print(min(ans))