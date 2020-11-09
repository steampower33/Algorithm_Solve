if __name__ == "__main__":
    N = int(input())

    num = 665
    count = 0

    while True:
        if N == count: break
        else:
            num += 1
            numL = list(str(num))
            for i in range(len(numL)-2):
                if numL[i] == numL[i+1] == numL[i+2] == '6':
                    count += 1
                    break

    print(num)