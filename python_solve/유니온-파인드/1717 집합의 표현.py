# 시간초과가 안뜨려면 아래 3줄을 추가해주어야한다.
# input과 print에서 다른 일을 더 처리하기때문에 그냥 사용하면 느리기때문이다.
import sys
input = sys.stdin.readline
print = sys.stdout.write

# 부모 찾기.
def getParent(zip, c):
    if c == zip[c]: return c
    zip[c] = getParent(zip, zip[c])
    return zip[c]

# 합집합.
def unionParent(zip, a, b):
    a = getParent(zip, a)
    b = getParent(zip, b)
    if a < b: zip[b] = a
    else: zip[a] = b

# 부모 찾기.
def findParent(zip, a, b):
    a = getParent(zip, a)
    b = getParent(zip, b)
    if a == b: print("YES\n")
    else: print("NO\n")

if __name__ == "__main__":
    # m = 연산의 개수.
    n, m = map(int, input().split())

    # n개의 집합
    zip = [int(i) for i in range(n+1)]

    # 0 = 합집합, 1 = 같은 집합인지 확인.

    for i in range(m):
        t, a, b = map(int, input().split())
        # 합집합 만들기.
        if t == 0:
            unionParent(zip, a, b)
        # 부모 동일 확인.
        else:
            findParent(zip, a, b)