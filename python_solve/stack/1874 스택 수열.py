

if __name__ == "__main__":
    n = int(input())

    # 1 2 3 4 5 6 7 8
    one_n = [i for i in range(1,n+1)]

    # 4 3 6 8 7 5 2 1
    Sequence = list()
    s = list()
    result = list()
    for _ in range(n): Sequence.append(int(input()))

    for i in range(len(Sequence)):
        cnt = 0
        while True:
            if len(s) >= 1:
                if s[-1] == Sequence[i]:
                    s.pop()
                    result.append('-')
                    break
            if len(one_n) == 0:
                break
            num = one_n[0]
            if num != Sequence[i]:
                one_n.remove(num)
                s.append(num)
                result.append('+')
            elif num == Sequence[i]:
                one_n.remove(num)
                result.append('+')
                result.append('-')
                break

    if len(s) == 0:
        for i in result:
            print(i)
    else:
        print('NO')
