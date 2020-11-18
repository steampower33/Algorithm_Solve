import sys

if __name__ == "__main__":
    n, k = map(int, input().split())
    coins = list()
    cnt = 0
    for i in range(n):
        coins.append(int(sys.stdin.readline()))

    while True:
        if k == 0:
            break

        lastBigMoney = coins[-1]

        if lastBigMoney > k:
            coins.pop()
        else:
            k -= lastBigMoney
            cnt += 1

    print(cnt)