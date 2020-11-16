import sys

if __name__ == "__main__":
    n = int(input())
    wires = list()
    dp = [1]*n
    for i in range(n):
        wires.append(list(map(int, sys.stdin.readline().rsplit())))

    wires.sort(key= lambda x: x[0])
    for i in range(n):
        for j in range(i):
            if wires[i][1] > wires[j][1]:
                dp[i] = max(dp[i], dp[j]+1)

    print(n-max(dp))