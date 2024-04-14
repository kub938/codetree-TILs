from collections import deque

dq = deque()

n = int(input())

for i in range(n):
    s = input()
    if s.startswith('push_back'):
        dq.appendleft(int(s[-1]))
    elif s.startswith('push_front'):
        dq.append(int(s[-1]))
    elif s.startswith('pop_front'):
        print(dq.pop())
    elif s.startswith('pop_back'):
        print(dq.popleft())
    elif s.startswith('size'):
        print(len(dq))
    elif s.startswith('empty'):
        if not dq:
            print(1)
        else:
            print(0)
    elif s.startswith('front'):
        print(dq[-1])
    elif s.startswith('back'):
        print(dq[0])