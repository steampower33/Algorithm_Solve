def dfs(i):
    global N, col, slash, backSlash, result
    if i == N:
        result += 1
        return
    for j in range(N):
        if not (col[j] or slash[i+j] or backSlash[i-j+N-1]):
            col[j] = slash[i + j] = backSlash[i - j + N - 1] = True
            dfs(i+1)
            col[j] = slash[i + j] = backSlash[i - j + N - 1] = False


if __name__ == "__main__":
    N = int(input())
    col, slash, backSlash = [False] * N, [False] * (2*N-1), [False] * (2*N-1)
    result = 0
    dfs(0)

    print(result)