import sys

class Stack(list):
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            return -1
        return self.items.pop()
    def is_empty(self):
        if len(self.items) == 0:
            return 1
        return 0
    def top(self):
        if self.is_empty():
            return -1
        return self.items[-1]
    def len(self):
        return len(self.items)

if __name__ == "__main__":
    n = int(input())
    s = Stack()
    for i in range(n):
        order = list(map(str, sys.stdin.readline().rsplit()))
        if order[0] == 'push':
            s.push(int(order[1]))
        elif order[0] == 'pop':
            print(s.pop())
        elif order[0] == 'top':
            print(s.top())
        elif order[0] == 'size':
            print(s.len())
        elif order[0] == 'empty':
            print(s.is_empty())
