N, L = int(input()), 1001
cnt_arr = [0] * L
for n in list(map(int, input().split())):
    cnt_arr[n] += 1

def insert_all(idx):
    for _ in range(cnt_arr[idx]):
        ret.append(idx)
    cnt_arr[idx] = 0
def insert_one(idx):
    ret.append(idx)
    cnt_arr[idx] -= 1

ret, idx = [], 0
while idx < L:
    if not cnt_arr[idx]:
        pass
    elif idx == L - 1 or not cnt_arr[idx + 1]:
        insert_all(idx)
    else:
        next = idx + 2
        while next < L and not cnt_arr[next]:
            next += 1
        if next >= L:
            insert_all(idx+1)
            insert_all(idx)
            break
        else:
            insert_all(idx)
            insert_one(next)
    idx += 1

for i in ret:
    print(i, end=' ')