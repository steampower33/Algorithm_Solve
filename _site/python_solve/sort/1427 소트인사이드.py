# 입력 받고.
s = list(map(int,input()))

# 내림 차순 정렬.
s.sort(reverse=True)

# 출력.
for i in s:
    print(i,end='')