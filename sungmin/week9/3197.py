from collections import deque

R, C = map(int, input().split())
DIR = [(-1,0), (0,-1), (0,1), (1,0)]

lake = [list(input()) for _ in range(R)]
ice = [list() for _ in range(1500)]
swan = list()
date = 0

def bfs_date():
    q = deque()
    for y in range(R):
        for x in range(C):
            if lake[y][x] == '.':
                q.append((y,x,0))
    while(q):
        (y,x,date) = q.popleft()
        for dy, dx in DIR:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < R and 0 <= nx < C): continue
            if lake[ny][nx] != 'X': continue
            lake[ny][nx] = date+1
            ice[date].append((ny,nx))
            q.append((ny,nx,date+1))

def is_valid_point(y, x, skip=0):
    global lake
    ret = list()
    for dy, dx in DIR:
        ny, nx = y + dy, x + dx
        if not (0 <= ny < R and 0 <= nx < C): continue
        if type(lake[ny][nx]) != tuple: continue
        if lake[y][x] == lake[ny][nx]: continue
        if skip: return True
        ret.append((ny, nx))
    return ret

def find_parent(p:tuple):
    global lake
    (y, x) = p
    if lake[y][x] != (y, x):
        lake[y][x] = find_parent(lake[y][x])
    return lake[y][x]

def union_parent(a:tuple, b:tuple):
    global lake
    a = find_parent(a)
    b = find_parent(b)
    if a > b:
        lake[a[0]][a[1]] = lake[b[0]][b[1]]
    elif a < b:
        lake[b[0]][b[1]] = lake[a[0]][a[1]]

def disjoint_set(taget):
    global lake
    for (y,x) in taget:
        lake[y][x] = (y,x)
        vp = is_valid_point(y,x)
        for p in vp:
            union_parent((y,x), p)

for y in range(R):
    for x in range(C):
        if lake[y][x] == 'L':
            swan.append((y,x))
            lake[y][x] = '.'
bfs_date()
target = list()
for y in range(len(lake)):
    for x in range(len(lake[y])):
        if lake[y][x] == '.':
            target.append((y,x))
disjoint_set(target)
while(find_parent(swan[0])) != (find_parent(swan[1])):
    disjoint_set(ice[date])
    print(lake)
    date += 1

print(date)