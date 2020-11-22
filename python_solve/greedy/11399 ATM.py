

if __name__ == "__main__":
    n = int(input())
    times = [_ for _ in map(int, input().split())]
    result = [0 for _ in range(n)]

    times.sort()
    result[0] = times[0]
    for i in range(1, n):
        result[i] = times[i] + result[i-1]

    print(sum(result))

