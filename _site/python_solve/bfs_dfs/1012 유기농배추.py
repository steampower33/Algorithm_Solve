from collections import deque

# bfs
# location -> (세로, 가로)
def bfs(field, location):

    # 전역변수로 설정.
    copy_field = field

    # 현재 위치의 값 0 으로 바꾸기.
    copy_field[location[0]][location[1]] = 0
    # 다음 위치 값을 설정해줄 값.
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # q를 설정하고, 거기에 location 위치를 넣는다.
    q = deque()
    q.append(location)

    # 무한 루프를 돌고.
    while True:
        # 두번째 q를 생성 및 초기화.
        q_second = deque()
        # q 안에 아무것도 없을때까지 돈다.
        while q:
            # q에 넣은 위치 값을 x_, y_에 넣어준다.
            y_, x_ = q.popleft()
            # 4방향으로 1이 있는지 검사.
            for i in range(4):
                # 검사할 다음 위치.
                nextY = y_ + dy[i] # 세로.
                nextX = x_ + dx[i] # 가로.

                # 총 범위안에 있고, 1인지 확인.
                if 0 <= nextY < len(copy_field) and 0 <= nextX < len(copy_field[0]) and field[nextY][nextX] == 1:
                    # 확인된 위치의 값을 0으로 만들어줌으로써, 밖에서 for문을 돌때 또 확인되서 count를 늘리지않게하기위함.
                    field[nextY][nextX] = 0
                    # 확인된 위치를 두번째 q에 넣어준다.
                    q_second.append((nextY, nextX))
        # q를 확인된 위치의 값들을 넣어둔 두번째 q로 바꿔준다.
        q = q_second
        # q가 비었다면, 종료.
        if not q: break

def main_():
    # 가로, 세로, 배추.
    m, n, k = map(int, input().split())
    # 밭 설정.
    field = [[0 for i in range(m)] for j in range(n)]
    # 밭 꾸미기.
    for i in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1
    #print(field)

    count = 0
    for i in range(n): # 세로.
        for j in range(m):# 가로.
            if field[i][j] == 1:
                # bfs들어갈때마다 count 하나씩 증가.
                bfs(field, (i,j))
                count += 1
    return count

if __name__ == "__main__":
    TestCase = int(input())

    for i in range(TestCase):
        print(main_())



