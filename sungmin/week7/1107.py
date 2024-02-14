N = int(input())
_ = int(input())
B = list(map(int, input().split()))

count = abs(100 - N)

for n in range(1000001): # N <= 500000 
    nstr, nlen = list(str(n)), len(str(n))

    err = 0
    for c in nstr:
        if int(c) in B:
            err = 1
            break

    if not err:
        count = min(count, abs(n - N) + nlen) # 숫자 누르기 + 플마 누르기

print(count)