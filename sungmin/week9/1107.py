N = int(input())
M = int(input())
B = list(map(int, input().split())) if M else []

ret = abs(N - 100)
for n in range(999999): # N <= 500000 
    nstr, nlen = list(str(n)), len(str(n))

    err = 0
    for c in nstr:
        if int(c) in B:
            err = 1
            break

    if not err:
        ret = min(ret, abs(N - n) + nlen) # 숫자 누르기 + 플마 누르기

print(ret)