# 가정한 횟수.
T = int(input())

# 정보.
for i in range(T):
    # 몇등인지.
    a, b = map(int, input().split())
    # 돈 설정.
    money = 0
    moneyA = {1: 5000000, 2: 3000000, 3: 2000000, 4: 500000, 5: 300000, 6: 100000}
    moneyB = {1: 5120000, 2: 2560000, 3: 1280000, 4: 640000, 5: 320000}

    # a에 해당하는 돈.
    for _ in range(1, 7):
        if a == 0:
            money += 0
            break
        if a <= _:
            money += moneyA[_]
            break
        a = a - _

    # b에 해당하는 돈.
    for _ in range(1,6):
        if b == 0:
            money += 0
            break
        count = 2 ** (_-1)
        if b <= count:
            money += moneyB[_]
            break
        b = b - count
    # 돈 출력.
    print(money)