import sys

if __name__ == "__main__":
    n = int(input())
    meetings = list()
    cnt = 1

    for i in range(n):
        times = list(map(int, sys.stdin.readline().rsplit()))
        meetings.append(times)

    meetings.sort(key=lambda x: [x[1], x[0]])

    last = meetings[0][1]
    for i in range(1,n):
        if last <= meetings[i][0]:
            cnt += 1
            last = meetings[i][1]

    print(cnt)