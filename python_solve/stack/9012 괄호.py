import sys

class Stack(list):
    def __init__(self):
        self.items = list()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def sPrint(self):
        for i in self.items:
            print(i, end=" ")
        print()

    def sClear(self):
        self.items.clear()

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        result = 1
        data = list(map(str,input()))
        s = Stack()
        for i in range(len(data)):
            if data[i] == '(':
                s.push(data[i])
            elif data[i] == ')':
                if s.isEmpty():
                    result = 0
                    break
                else:
                    s.pop()

        if s.isEmpty() and result == 1:
            print("YES")
        else:
            print("NO")

        s.clear()