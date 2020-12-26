import sys

def paperSum(x, y):
    sum = 0
    for i in range(y[0], y[1]):
        for j in range(x[0], x[1]):
            sum += paper[i][j]
    return sum

def paperChecker(x, y, p):
    global zero, one
    value = (x[1] - x[0]) * (y[1] - y[0])
    pS = paperSum(x,y)
    if  pS == value:
        one += 1
        return
    elif pS == 0:
        zero += 1
        return
    elif paperSum(x,y) != value:
        paperChecker([x[0], x[1] - p//2], [y[0],y[1] - p//2], p//2)

        paperChecker([x[0] + p//2, x[1]], [y[0], y[1] - p//2], p//2)

        paperChecker([x[0], x[1] - p//2], [y[0] + p//2, y[1]], p//2)

        paperChecker([x[0] + p//2, x[1]], [y[0] + p//2, y[1]], p//2)

if __name__ == "__main__":
    zero = 0
    one = 0
    n = int(sys.stdin.readline())
    paper = [[] for j in range(n)]

    for _ in range(n): paper[_] = list(map(int, sys.stdin.readline().rstrip('\n').rsplit()))
    paperChecker([0,n], [0,n], n)

    print(zero)
    print(one)