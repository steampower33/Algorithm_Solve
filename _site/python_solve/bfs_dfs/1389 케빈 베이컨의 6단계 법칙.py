# 입력.
n, m = map(int, input().split())
# 테이블.
map_ = [[n for _ in range(n)] for _ in range(n)]

# 테이블에 양방향으로 연결.
for _ in range(m):
    a, b = map(int, input().split())
    map_[a-1][b-1] = 1
    map_[b-1][a-1] = 1

#플로이드-워셜 알고리즘
for k in range(n):
    for i in range(n):
        for j in range(n):
            # 대각선, 자기 자신끼리는 가중치 0
            if i == j:
                map_[i][j] = 0
            else:
            # 최소값을 적용.
                map_[i][j] = min(map_[i][j], map_[i][k] + map_[k][j])

#출력
bacon = []
for row in map_:
    bacon.append(sum(row))
print(bacon.index(min(bacon)) + 1)