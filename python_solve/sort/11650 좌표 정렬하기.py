import sys; input = sys.stdin.readline # 입력 빠르게.
n = int(input()); loc = list() # 입력 및 위치 설정.
for _ in range(n): loc.append(list(map(int, input().split()))) # 위치 넣기.
loc.sort(key=lambda dot: (dot[0], dot[1])) # x를 먼저 기준, y를 그 다음 기준으로 정렬.
for [i, j] in loc: print(i, j) # 출력.