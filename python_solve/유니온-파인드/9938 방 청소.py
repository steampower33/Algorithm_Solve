# 입/출력 빠르게.
import sys
input = sys.stdin.readline

# 부모 찾기.
def find(x):
    if(p[x]==x): return x
    p[x] = find(p[x])
    return p[x]

# 합집합.
def merge(x,y):
    # 부모찾고,
    x,y = find(x),find(y)
    # x를 부모로 섬김.
    p[y]=x
    # x를 부모로 섬기므로, y의 맥스와 지금을 모두 0으로 만들어준다.
    max_p[y]=0
    now_p[y]=0

# 입력 설정.
n,l=map(int,input().split())
# 부모 설정.
p=[i for i in range(l+1)]
# 한 부모가 수용가능한 수.
# 즉 1,2 이랑 연결되면 부모는 최대 2를 수용할수있다.
# 여기서 2,3이 되면 최대 3을 수용할수있음.
# 지금과 max가 다르면 보관할수있고,
# 같으면 보관할수 없으므로, 먹어야한다.
#
max_p=[1]*(l+1)
now_p=[0]*(l+1)

for i in range(n):
    a,b = map(int,input().split())
    # a의 부모와 b의 부모가 다르면,
    if find(p[a])!=find(p[b]):
        # a의 부모의 최대와 지금에다가 b 부모의 최대와 지금을 더해준다.
        max_p[find(p[a])]+=max_p[find(p[b])]
        now_p[find(p[a])]+=now_p[find(p[b])]
        # 그뒤 merge를 통해 합집합과정을 거쳐준다.
        merge(a,b)
    # 지금이랑 최대의 값이 같으면 더이상 보관불가능함.
    if now_p[find(a)]==max_p[find(a)]:print('SMECE')
    # 다르면 보관가능하니까 지금위치에 1더해줌.
    else:now_p[find(a)]+=1;print('LADICA')