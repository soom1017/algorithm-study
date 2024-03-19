import sys
input = sys.stdin.readline

n = int(input()) # 전체 사람 수
target1, target2 = map(int, input().split()) # 촌수를 계산할 사람 번호

m = int(input()) # 부모-자식 관계 개수

relationships = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    x, y =  map(int, input().split())
    relationships[x].append(y)
    relationships[y].append(x)

chonsu_calculated = -1

def dfs(node, chonsu):
    visited[node] = True
    chonsu += 1

    if node == target2:
        global chonsu_calculated
        chonsu_calculated = chonsu
    
    for relation in relationships[node]:
        if not visited[relation]:
            dfs(relation, chonsu)

dfs(target1, 0)

print(chonsu_calculated if chonsu_calculated == -1 else (chonsu_calculated - 1))