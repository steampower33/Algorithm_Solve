from collections import deque

def bfs(field, start):
    queue = deque()
    count = 1
    queue.append(start)

    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]

    while True:
        q_second = deque()
        while queue:
            y_, x_ = queue.popleft()
            #print(y_,x_)
            for i in range(8):
                nextX = dx[i] + x_
                nextY = dy[i] + y_

                if 0 <= nextX < len(field[0]) and 0 <= nextY < len(field) and field[nextY][nextX] == 1:
                    count += 1
                    field[nextY][nextX] = 0
                    q_second.append((nextY, nextX))
        #print(count)

        queue = q_second
        if not queue: break
    if count > 0:
        return 1
    else:
        return 0


if __name__ == "__main__":

    w, h = -1, -1
    islands = list()
    while w != 0 and h !=0 :
        # 너비, 높이.
        w,h = map(int, input().split())

        field = [[int(i) for i in input().split()] for j in range(h)]

        #print(field)
        num = 0
        # 높이.
        for i in range(h):
            # 너비.
            for j in range(w):
                # 세로, 가로.
                if field[i][j] == 1:
                    a = bfs(field, (i,j))
                    num += int(a)

        islands.append(num)

    #print(islands)
    for i in range(len(islands)-1):
        print(islands[i])