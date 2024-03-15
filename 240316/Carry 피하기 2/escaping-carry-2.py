n = int(input())
arr = [input() for _ in range(n)]
no_carry = []

def check_carry(a,b,c):
    cnt=0
    max_len = max(len(a),len(b),len(c))
    if len(a)<max_len or len(b)<max_len or len(c)<max_len:
        a=a.zfill(max_len)
        b=b.zfill(max_len)
        c=c.zfill(max_len)
        
    for i in range(max_len):
        na,nb,nc = int(a[i]),int(b[i]),int(c[i])
        sum_value = na+nb+nc
        if sum_value>=10:
            cnt+=1
    if cnt==0:
        return True
    elif cnt>0:
        return False

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if check_carry(arr[i],arr[j],arr[k]):
                no_carry.append(int(arr[i])+int(arr[j])+int(arr[k]))

if not no_carry:
    print(-1)
else:
    print(max(no_carry))