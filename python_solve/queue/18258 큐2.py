import collections
import sys

class Queue():
    def __init__(self):
        self.items = collections.deque()

    def push(self, x):
        self.items.append(int(x))

    def pop(self):
        if self.isEmpty():
            print('-1')
        else:
            print(self.items.popleft())

    def front(self):
        if self.isEmpty():
            print('-1')
        else:
            print(self.items[0])

    def back(self):
        if self.isEmpty():
            print('-1')
        else:
            print(self.items[-1])

    def size(self):
        print(len(self.items))

    def isEmpty(self):
        if len(self.items) == 0:
            return 1
        else:
            return 0

if __name__ == "__main__":

    N = int(input())
    Q = Queue()

    for _ in range(N):
        commands = list(sys.stdin.readline().rsplit())
        if commands[0] == 'push':
            Q.push(commands[1])
        elif commands[0] == 'pop':
            Q.pop()
        elif commands[0] == 'front':
            Q.front()
        elif commands[0] == 'back':
            Q.back()
        elif commands[0] == 'empty':
            print(Q.isEmpty())
        elif commands[0] == 'size':
            Q.size()