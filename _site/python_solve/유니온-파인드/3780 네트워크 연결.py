# 입력 빠르게, 이거 않하면 시간초과.
import sys
input = sys.stdin.readline

# 부모 찾기.
def find(x):
    if p[x] == x: return x
    # 교체하기.
    tmp = find(p[x])
    len_p[x] += len_p[p[x]]
    p[x] = tmp
    return tmp
    # 아래는 이전의 코드. 비슷해 보이지만 아래는 오답이 발생한다.
    # len_p[x] += len_p[p[x]]
    # p[x] = find(p[x])
    # return p[x]

# 합치기.
def merge(a, b):
    # a에 길이를 저장.
    len_p[a] = abs(a - b) % 1000
    # b가 부모.
    p[a] = b

# 테스트케이스만큼.
for i in range(int(input())):
    n = int(input())
    # 부모, 길이.
    p = [int(i) for i in range(n + 1)]
    len_p = [0] * (n + 1)
    # O가 입력될때까지.
    while True:
        s = input().split()
        if s[0] == 'E':
            find(int(s[1]))
            print(len_p[int(s[1])])
        elif s[0] == 'I':
            a,b = int(s[1]),int(s[2])
            merge(a, b)
        else:
            break



