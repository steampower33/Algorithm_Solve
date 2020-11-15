import sys

if __name__ == "__main__":
    n = int(input())
    wires = list()
    for i in range(n):
        wires.append(list(map(int,sys.stdin.readline().rsplit())))

    crossWiresCnt = dict()
    for i in range(1, n+1):
        crossWiresCnt[i] = 0

    for i in range(n):
        for j in range(n):
            if i == j: continue
            if