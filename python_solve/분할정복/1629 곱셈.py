def solve(a,b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        if b % 2 == 1:
            return solve(a, b - 1) * a
        elif b % 2 == 0:
            result = solve(a, b // 2)
            return result * result % c

if __name__ == "__main__":

    a, b, c = map(int, input().split())

    print(solve(a,b) % c)