import collections

if __name__ == "__main__":
    n, k = map(int, input().split())

    circle = collections.deque([_ for _ in range(1,n+1)])
    result = list()
    cnt = 1
    while len(circle) != 0:
        if cnt // k >= 1 and cnt % k == 0:
            result.append(circle.popleft())
        else:
            circle.rotate(-1)
        cnt += 1

    print("<", end = '')
    for _ in range(len(result)):
        if _ == len(result)-1:
            print(result[_], end='>')
        else:
            print(result[_], end=', ')