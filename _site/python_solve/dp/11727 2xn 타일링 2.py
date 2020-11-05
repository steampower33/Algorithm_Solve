import sys
input = sys.stdin.readline
print = sys.stdout.write

if __name__ == "__main__":
    n = int(input())
    squares = [0] * 1001
    squares[1] = 1
    squares[2] = 3
    for i in range(3, n+1):
        squares[i] = squares[i-1] + squares[i-2] * 2

    print(str(squares[n] % 10007))