# 정점의 개수.
# 버스의 개수.
n = int(input())
m = int(input())

# 무한대 및 그래프 설정.
INF = 987654321
field = [[INF for i in range(n)] for j in range(n)]

# 버스의 정보 입력받는다.
# 함정이 있다 입력받을때 이미 정보가 있는 위치에 그 위치의 값보다 작은 값을 입력받을수있다.
for _ in range(m):
    a, b, c = map(int, input().split())
    field[a-1][b-1] = min(field[a-1][b-1], c)

# 플로이드.
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                field[i][j] = 0
            if field[i][k] + field[k][j] < field[i][j]:
                field[i][j] = field[i][k] + field[k][j]

# 출력.
for i in range(n):
    for j in range(n):
        print(field[i][j], end=" ")
    print()