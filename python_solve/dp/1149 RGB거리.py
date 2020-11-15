import sys

if __name__ == "__main__":
    n = int(input())
    rgb = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(n)]

    d = [[0 for i in range(3)] for j in range(n)]
    d[0] = rgb[0]
    for i in range(1, n):
        d[i][0] = min(d[i - 1][1], d[i - 1][2]) + rgb[i][0]
        d[i][1] = min(d[i - 1][0], d[i - 1][2]) + rgb[i][1]
        d[i][2] = min(d[i - 1][0], d[i - 1][1]) + rgb[i][2]

    print(min(d[n-1]))
