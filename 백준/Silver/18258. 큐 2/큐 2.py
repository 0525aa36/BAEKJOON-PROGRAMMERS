import sys
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque() 

    def push(self, x):
        self.queue.append(x)  # 뒤에 추가

    def pop(self):
        if self.empty():
            return -1
        else:
            return self.queue.popleft()  # 선입선출

    def size(self):
        return len(self.queue)  # 큐 길이

    def empty(self):
        if len(self.queue) == 0:
            return 1
        else:
            return 0

    def front(self):
        if self.empty():
            return -1
        else:
            return self.queue[0]  # 맨 앞

    def back(self):
        if self.empty():
            return -1
        else:
            return self.queue[-1]  # 맨 뒤

queue = Queue()


n = int(sys.stdin.readline())

for _ in range(n):
    명령 = sys.stdin.readline().strip().split()
    
    if 명령[0] == "push":
        queue.push(명령[1])

    elif 명령[0] == "pop":
        print(queue.pop())

    elif 명령[0] == "size":
        print(queue.size())

    elif 명령[0] == "empty":
        print(queue.empty())

    elif 명령[0] == "front":
        print(queue.front())
        
    elif 명령[0] == "back":
        print(queue.back())
