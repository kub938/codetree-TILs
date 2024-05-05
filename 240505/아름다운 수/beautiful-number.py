n = int(input())
cnt = 0
arr = []
check = False

def b_num(c):
    global cnt
    global check
    if n==c:
        if arr.count(1)%1==0 and arr.count(2)%2==0 and arr.count(3)%3==0 and arr.count(4)%4==0:
            check = True
        if check:
            cnt+=1
            check = False
            return
    
    for i in range(1,5):
        arr.append(i)
        b_num(c+1)
        arr.pop()

b_num(1)
print(cnt)