import collections

if __name__ == "__main__":
    q = collections.deque()

    for _ in range(1, int(input())+1):
        q.append(_)


    while len(q) != 1:

        q.popleft()
        q.append(q.popleft())

    print(q.popleft())