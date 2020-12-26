import collections, sys

if __name__ == "__main__":

    n = int(sys.stdin.readline())
    deque = collections.deque()

    for _ in range(n):
        commands = list(sys.stdin.readline().rsplit())

        if commands[0] == 'push_front':
            deque.appendleft(int(commands[1]))
        elif commands[0] == 'push_back':
            deque.append(int(commands[1]))
        elif commands[0] == 'pop_front':
            if len(deque) == 0:
                print("-1")
            else:
                print(deque.popleft())
        elif commands[0] == 'pop_back':
            if len(deque) == 0:
                print("-1")
            else:
                print(deque.pop())
        elif commands[0] == 'size':
            print(len(deque))
        elif commands[0] == 'empty':
            if len(deque) == 0:
                print(1)
            else:
                print(0)
        elif commands[0] == 'front':
            if len(deque) == 0:
                print("-1")
            else:
                print(deque[0])
        elif commands[0] == 'back':
            if len(deque) == 0:
                print("-1")
            else:
                print(deque[-1])