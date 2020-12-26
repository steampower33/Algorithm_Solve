import collections, sys

if __name__ == "__main__":

    t = int(sys.stdin.readline())

    for _ in range(t):
        n, m = map(int, sys.stdin.readline().rsplit())
        importance = collections.deque(map(int, sys.stdin.readline().rsplit()))
        cnt = 0
        des = list(sorted(importance))
        # print(des)
        for _ in range(len(importance)):
            importance[_] = (_, importance[_])

        # print(importance)
        while True:

            if importance[0][1] == des[-1]:
                cnt += 1
                des.pop()
                if importance[0][0] == m:
                    print(cnt)
                    break
                importance.popleft()
            elif importance[0][1] < des[-1]:
                importance.rotate(-1)
