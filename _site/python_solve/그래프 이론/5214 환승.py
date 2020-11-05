C, T = 101001, 10**5
from collections import deque
N, K, M = map(int, input().split())
g = [[] for i in range(C)]
v = [0]*C
for i in range(1,M+1):
    s = list(map(int, input().split()))
    for k in s:
        g[k].append(T+i)
        g[T+i].append(k)
q = deque([1])
v[1] = 1
while q:
    c = q.popleft()
    for i in g[c]:
        if not v[i]:
            q.append(i)
            v[i] = v[c]+1 if c>T else v[c]
print(v[N] if v[N]else -1)