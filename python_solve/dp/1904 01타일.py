
if __name__ == "__main__":
    n = int(input())

    cache = [0 for i in range(1000001)]

    cache[1] = 1
    cache[2] = 2

    for i in range(3, n+1):
        cache[i] = (cache[i-2] + cache[i-1]) % 15746

    print(cache[n])