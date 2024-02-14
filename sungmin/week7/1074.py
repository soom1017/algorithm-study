def recul(n, y, x):
    if n == 0: return 1

    p = pow(2, n - 1)
    align = pow(p, 2)

    ret = 0
    if y < p and x < p: # 1사분면
        ret += recul(n - 1, y, x)
        ret += align * 0
    elif y < p and x >= p: # 2사분면
        ret += recul(n - 1, y, x - p)
        ret += align * 1
    elif y >= p and x < p: # 3사분면
        ret += recul(n - 1, y - p, x)
        ret += align * 2
    elif y >= p and x >= p: # 4사분면, else
        ret += recul(n - 1, y - p, x - p)
        ret += align * 3

    return ret

N, r, c = map(int, input().split())
print(recul(N, r, c) - 1)