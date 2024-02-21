import sys

def find_parent(x): # 부모 노드 찾기
    if x != parents[x]:
        return find_parent(parents[x])
    return x

def union_parent(n1, n2): # 두 노드 연결
    n1 = find_parent(n1)
    n2 = find_parent(n2)
    if n1 < n2: # 노드의 번호가 작은 노드에 연결
        parents[n2] = n1
    else:
        parents[n1] = n2

n, m = map(int, input().split())
parents = [i for i in range(n)] # 부모 노드를 알려주는 배열
edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]

for idx, info in enumerate(edges):
    if find_parent(info[0]) != find_parent(info[1]): # 부모 노드가 서로 다르면 연결
        union_parent(info[0], info[1])
    else: # 사이클 발생
        print(idx+1)
        break
else:
    print(0)