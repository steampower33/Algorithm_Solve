# 정점 개수.
n = int(input())

# 그래프 입력.
field = [[int(i) for i in input().split()] for j in range(n)]

# 플로이드 와샬.
# 그래프 돌면서 i -> j -> j 가 가능한지 판별한 다음
# i -> j 의 값을 1로 설정.
for k in range(n):
    for i in range(n):
        for j in range(n):
            if field[i][k] and field[k][j]:
                field[i][j] = 1

# 바뀐 그래프 출력.
for i in range(len(field)):
    for j in range(len(field[i])):
        print(field[i][j],end=" ")
    print()
