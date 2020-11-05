import sys
input = sys.stdin.readline
print = sys.stdout.write

def dictReset(dict):
    for i in range(1, len(dict)+1): dict[i] = 0

def dfs(a):
    visited[a] = 1
    for b in graph[a]:
        if B[b] == 0 or visited[B[b]] == 0 and dfs(B[b]):
            A[a] = b; B[b] = a
            return 1
    return 0

if __name__ == "__main__":
    # 직원은 1번부터 n번까지 번호
    # 일은 1 번부터 m번까지 번호
    # 각 직원은 한개의 일
    # 각각의 일을 담당하는 사람은 1명
    # 각각의 직원이 할 수 있는 일의 목록이 주어짐 -> m개의 일중에서 최대 몇개 가능 한가?

    n, m = map(int, input().split()); graph = dict(); visited = dict(); A = dict(); B = dict(); match = 0
    for i in range(1, 1001): graph[i] = list(); visited[i] = 0; A[i] = 0; B[i] = 0

    # 1번 부터 n 번 직원들이 각각 할수잇는 일의 수와 일의 번호가 주어진다.
    for i in range(1, n+1):
        s = input().split()
        for j in range(1, len(s)):
            graph[i].append(int(s[j]))

    for i in range(1, n+1):
        if A[i] == 0:
            dictReset(visited)
            if dfs(i): match += 1

    print(str(match))

