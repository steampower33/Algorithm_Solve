import sys

def treeSum(x, y):
    sum = 0
    for i in range(y[0], y[1]):
        for j in range(x[0], x[1]):
            sum += tree[i][j]
    return sum

def treeChecker(x, y, p):
    global result
    value = (x[1] - x[0]) * (y[1] - y[0])
    pS = treeSum(x,y)
    if  pS == value:
        result.append('1')
        return
    elif pS == 0:
        result.append('0')
        return
    elif treeSum(x,y) != value:
        result.append('(')
        treeChecker([x[0], x[1] - p//2], [y[0],y[1] - p//2], p//2)

        treeChecker([x[0] + p//2, x[1]], [y[0], y[1] - p//2], p//2)

        treeChecker([x[0], x[1] - p//2], [y[0] + p//2, y[1]], p//2)

        treeChecker([x[0] + p//2, x[1]], [y[0] + p//2, y[1]], p//2)
        result.append(')')

if __name__ == "__main__":
    result = list()
    n = int(sys.stdin.readline())
    tree = [[] for j in range(n)]

    for _ in range(n): tree[_] = list(map(int, sys.stdin.readline().rstrip('\n')))

    treeChecker([0,n], [0,n], n)

    for _ in result:
        print(_, end='')