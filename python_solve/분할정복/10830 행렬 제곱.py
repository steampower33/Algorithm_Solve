import sys

def mul_matrix(a, matrix):
    global n
    result_matrix = [[0 for _ in range(n)]for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result_matrix[i][j] += (a[i][k] * matrix[k][j])
            result_matrix[i][j] %= 1000

    return result_matrix

def solve(a, b):
    if b == 1:
        for i in range(n):
            for j in range(n):
                a[i][j] %= 1000
        return a
    elif b % 2 == 1:
        matrix = solve(a, b-1)
        new_matrix = mul_matrix(a, matrix)

        return new_matrix
    else:
        matrix = solve(a, b//2)
        new_matrix = mul_matrix(matrix, matrix)

        return new_matrix

if __name__ == "__main__":
    n, b = map(int, sys.stdin.readline().split())
    a = [[] for i in range(n)]
    for i in range(n): a[i] = list(map(int, sys.stdin.readline().split()))

    result = solve(a,b)

    for row in result:
        print(*row)
