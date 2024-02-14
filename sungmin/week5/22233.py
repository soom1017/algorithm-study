import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def hashing_1(keyword):
    return ord(keyword[0]) % 16

def hashing_2(keyword):
    return ord(keyword[-1]) % 16

keywords = [[list()] * 16] * 16
for _ in range(N):
    keyword = input()[:-1]
    keywords[hashing_1(keyword)][hashing_2(keyword)].append(keyword)

count = N
for _ in range(M):
    writings = input()[:-1].split(',')
    for write in writings:
        y, x = hashing_1(keyword), hashing_2(keyword)
        if write in keywords[y][x]:
            keywords[y][x].remove(write)
            count -= 1
    print(count)
