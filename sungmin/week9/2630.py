N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]

w, b = 0, 0

def DP(ys, ye, xs, xe):
    global w, b
    
    color, diff = MAP[ys][xs], 0
    
    for y in range(ys, ye + 1):
        for x in range(xs, xe + 1):
            if color != MAP[y][x]:
                diff = 1
                break
    
    if diff:
        ym, xm = (ys + ye) // 2, (xs + xe) // 2
        DP(ys, ym, xs, xm)
        DP(ym + 1, ye, xs, xm)
        DP(ys, ym, xm + 1, xe)
        DP(ym + 1, ye, xm + 1, xe)
    
    else:
        if color: b += 1
        else: w += 1

    return

DP(0, N - 1, 0, N - 1)
print(w)
print(b)