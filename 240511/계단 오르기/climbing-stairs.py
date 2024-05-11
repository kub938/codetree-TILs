n = int(input())

def cal(n):
    if n==0:
        cnt+=1
        return
    cal(n-2)
    cal(n-3)

cnt=0

if n<=3:
    print(1)
else:
    cal(n)
    print(cnt)