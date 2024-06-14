hashmap = {}

def add(k,v):
    hashmap[k]=v

def remove(k):
    hashmap.pop(k)

def find(k):
    if k in hashmap:
        print(hashmap[k])
    else:
        print('None')


n = int(input())

for i in range(n):
    data = input().split()
    o,k = data[0],int(data[1])
    if o=='add':
        v = int(data[2])
        add(k,v)
    elif o=='remove':
        remove(k)
    else:
        find(k)