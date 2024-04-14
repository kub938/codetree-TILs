# from collections import deque

# class Queue:
#     def __init__(self):
#         self.dq = deque()

#     def push(self, item):
#         self.dq.append(item)
    
#     def empty(self):
#         return not self.dq
    
#     def size(self):
#         return len(self.dq)
    
#     def pop(self):
#         if self.empty():
#             raise Exception('Queue is empty')

#         return self.dq.popleft()
    
#     def front(self):
#         if self.empty():
#             raise Exception('Queue is empty')

#         return self.dq[0]

from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()

    def push(self, item):
        self.dq.append(item)

    def pop(self):
        if self.empty():
            raise Exception('Queue is empty')
        return self.dq.popleft()
    
    def size(self):
        return len(self.dq)

    def empty(self):
        return not self.dq

    def front(self):
        if self.empty():
            raise Exception('Queue is empty')
        return self.dq[0]

    def print_q(self):
        print(list(self.dq))
q = Queue()

n = int(input())
arr = [list(input().split()) for _ in range(n)]

for elem in arr:
    if elem[0]=='push':
        q.push(int(elem[1]))
    elif elem[0]=='pop':
        print(q.pop())
    elif elem[0]== 'size':
        print(q.size())
    elif elem[0] == 'empty':
        print(1 if q.empty() else 0)
    else:
        print(q.front())