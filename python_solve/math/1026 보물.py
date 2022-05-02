

def treasure():
    n = int(input())

    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())), reverse=True)

    s = 0
    for _ in range(n):
        s += a[_] * b[_]

    print(s)

treasure()