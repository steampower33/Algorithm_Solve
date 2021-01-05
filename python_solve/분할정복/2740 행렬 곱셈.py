import sys

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    a = [[] for _ in range(n)]
    for i in range(n): a[i] = list(map(int, sys.stdin.readline().split()))

    m, k = map(int, sys.stdin.readline().split())
    b = [[] for _ in range(m)]
    for i in range(m): b[i] = list(map(int, sys.stdin.readline().split()))

    r = [[0 for i in range(k)] for j in range(n)]

    for i in range(n):
        for j in range(k):
            num = 0
            for l in range(m):
                num += a[i][l] * b[l][j]
            r[i][j] = num

    for i in range(n):
        for j in range(k):
            print(r[i][j], end=' ')
        print()