if __name__ == "__main__":
    testCase = int(input())
    for i in range(testCase):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        d = (abs(x1-x2) ** 2 + abs(y1-y2) ** 2) ** 0.5
        if r2 >= r1:
            if r2 - r1 < d < r1 + r2: print("2")
            elif d == r1 + r2 or (d == r2 - r1 and d != 0): print("1")
            elif d < r2 - r1 or d > r1 + r2: print("0")
            elif d ==0 and r1 == r2: print("-1")
        else:
            if r1 - r2 < d < r1 + r2: print("2")
            elif d == r1 + r2 or (d == r1 - r2 and d != 0): print("1")
            elif d < r1 - r2 or d > r1 + r2: print("0")
            elif d ==0 and r1 == r2: print("-1")