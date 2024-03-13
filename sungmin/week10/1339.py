N = int(input())

count = dict()
for _ in range(N):
    words = list(input())
    for i, char in enumerate(reversed(words)):
        if char not in list(count.keys()):
            count[char] = 10 ** i
        else: 
            count[char] += 10 ** i
count = sorted(list(count.values()), reverse=True)

ret = 0
mul = list(range(9, -1, -1))
for i, v in enumerate(count):
    ret += v * mul[i]
print(ret)