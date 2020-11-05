
if __name__ == "__main__":
    N = int(input())

    Constructor = 0
    for i in range(N+1):
        nums = list(map(int, list(str(i))))
        Decomposition = i + sum(nums)

        if Decomposition == N:
            Constructor = i
            break

    if Constructor == 0:
        print("0")
    else:
        print(Constructor)

