

if __name__ == "__main__":
    t = int(input())
    cache = [(0,0) for i in range(41)]

    cache[0] = (1,0)
    cache[1] = (0,1)

    for i in range(2, 41):
        cache[i] = (cache[i-2][0] + cache[i-1][0], cache[i-2][1] + cache[i-1][1])

    for i in range(t):
        idx = int(input())
        print(cache[idx][0], cache[idx][1])