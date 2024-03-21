arr = list(map(int,input().split()))
n = len(arr)
check = True
diff = 5000

for i in range(n):
    for j in range(i+1,n):
        for k in range(n):
            for l in range(k+1,n):
                if k==i or k==j or l==i or l==j:
                    continue
                else:
                    check = False

                    sum1 = 0
                    sum2 = 0
                    sum3 = 0

                    sum1 = arr[i]+arr[j]
                    sum2 = arr[k]+arr[l]
                    sum3 = sum(arr)-(sum1+sum2)
                    if sum1==sum2 or sum2==sum3 or sum1==sum3:
                        check = True
                        continue

                    diff = min(diff, max(sum1,sum2,sum3)-min(sum1,sum2,sum3))

if check:
    print(-1)
else:
    print(diff)