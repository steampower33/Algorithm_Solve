if __name__ == "__main__":
    h, w = map(int, input().split())
    chess = [[i for i in input()] for j in range(h)]
    countB = 0
    countW = 0
    min = 987654321
    for i in range(h-7):
        for j in range(w-7):
            countB = 0
            countW = 0
            for k in range(i, i+8):
                for l in range(j, j+8):
                    if (k + l) % 2 == 0:
                        if chess[k][l] == 'W':
                            countW += 1
                        else:
                            countB += 1
                    else:
                        if chess[k][l] == 'B':
                            countW += 1
                        else:
                            countB += 1

            if min > countB: min = countB
            if min > countW: min = countW
    print(min)