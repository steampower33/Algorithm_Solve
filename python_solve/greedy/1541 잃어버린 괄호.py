
if __name__ == "__main__":
    exp = input().split('-')
    result = 0

    for i in exp[0].split('+'):
        result += int(i)

    for i in range(1, len(exp)):
        for j in exp[i].split('+'):
            result -= int(j)

    print(result)