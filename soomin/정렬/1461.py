# 도서관: https://acmicpc.net/problem/1461
from bisect import bisect_left

n, m = map(int, input().split())
books = list(map(int, input().split()))

books.sort()

result = 0
if books[0] * books[-1] < 0:
    # 다른 방향에 책 존재
    x = bisect_left(books, 0)
    for i in range(0, x, m):
        result -= books[i]
    for i in range(n-1, x-1, -m):
        result += books[i]
elif books[0] < 0:
    # 음수에만 존재
    for i in range(0, n, m):
        result -= books[i]
else:
    # 양수에만 존재
    for i in range(n-1, -1, -m):
        result += books[i]

result *= 2
leftmost, rightmost = abs(books[0]), abs(books[-1])
if leftmost < rightmost:
    result -= rightmost
else:
    result -= leftmost

print(result)