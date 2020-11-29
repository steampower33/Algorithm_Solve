import sys

class Stack(list):
    def __init__(self):
        self.items = list()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def sum(self):
        return sum(self.items)

if __name__ == "__main__":
    k = int(input())
    s = Stack()

    for i in range(k):
        num = int(sys.stdin.readline())
        if num == 0:
            s.pop()
        else:
            s.push(num)

    print(s.sum())