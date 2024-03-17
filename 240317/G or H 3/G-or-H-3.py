import sys

n,k =map(int,input().split())
n_arr = []
alp_arr = []
num,alp = 0,''
score = {'G':1,'H':2,0:0}
sum_score = 0
max_score = -sys.maxsize

for i in range(n):
    num, alp = input().split()
    n_arr.append(num)
    alp_arr.append(alp)

n_arr = list(map(int,n_arr))
n = max(n_arr)
if n<k:
    n=k

arr = [0 for _ in range(n+1)]

for i,a in zip(n_arr,alp_arr):
    arr[i] = a

for i in range(n-k+1):
    sum_score = 0
    for j in range(i,i+k+1):
        sum_score+=score[arr[j]]
    max_score = max(max_score,sum_score)

print(max_score)