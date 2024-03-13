
N, M, K = map(int, input().split())

board = [list(input()) for _ in range(N)]
board_black = [[0 for _ in range(M)] for _ in range(N)]
board_white = [[0 for _ in range(M)] for _ in range(N)]

for y in range(N):
    for x in range(M):
        if board[y][x] == "B":
            if (y + x) % 2:
                board_black[y][x] = 1
                board_white[y][x] = 0
            else:
                board_black[y][x] = 0
                board_white[y][x] = 1
        if board[y][x] == "W":
            if (y + x) % 2:
                board_black[y][x] = 0
                board_white[y][x] = 1
            else:
                board_black[y][x] = 1
                board_white[y][x] = 0

board_black_sum = [[0 for _ in range(M)] for _ in range(N)]
board_white_sum = [[0 for _ in range(M)] for _ in range(N)]

board_black_sum[0][0] = board_black[0][0]
board_white_sum[0][0] = board_white[0][0]

for y in range(1, N):
    board_black_sum[y][0] = board_black[y][0] + board_black_sum[y - 1][0]
    board_white_sum[y][0] = board_white[y][0] + board_white_sum[y - 1][0]

for x in range(1, M):
    board_black_sum[0][x] = board_black[0][x] + board_black_sum[0][x - 1]
    board_white_sum[0][x] = board_white[0][x] + board_white_sum[0][x - 1]

for y in range(1, N):
    for x in range(1, M):
        board_black_sum[y][x] = board_black[y][x] + board_black_sum[y - 1][x] + board_black_sum[y][x - 1] - board_black_sum[y - 1][x - 1]
        board_white_sum[y][x] = board_white[y][x] + board_white_sum[y - 1][x] + board_white_sum[y][x - 1] - board_white_sum[y - 1][x - 1]

board_black_diff = [[0 for _ in range(M)] for _ in range(N)]
board_white_diff = [[0 for _ in range(M)] for _ in range(N)]

board_black_diff[K - 1][K - 1] = board_black_sum[K - 1][K - 1]
board_white_diff[K - 1][K - 1] = board_white_sum[K - 1][K - 1]

for y in range(K, N):
    board_black_diff[y][K - 1] = board_black_sum[y][K - 1] - board_black_sum[y - K][K - 1]
    board_white_diff[y][K - 1] = board_white_sum[y][K - 1] - board_white_sum[y - K][K - 1]
for x in range(K, M):
    board_black_diff[K - 1][x] = board_black_sum[K - 1][x] - board_black_sum[K - 1][x - K]
    board_white_diff[K - 1][x] = board_white_sum[K - 1][x] - board_white_sum[K - 1][x - K]

for y in range(K, N):
    for x in range(K, M):
        board_black_diff[y][x] = board_black_sum[y][x] + board_black_sum[y - K][x - K] - board_black_sum[y - K][x] - board_black_sum[y][x - K]
        board_white_diff[y][x] = board_white_sum[y][x] + board_white_sum[y - K][x - K] - board_white_sum[y - K][x] - board_white_sum[y][x - K]

black = min([min(i[K-1:]) for i in board_black_diff[K-1:]])
white = min([min(i[K-1:]) for i in board_white_diff[K-1:]])

print(min(black, white))

# 진짜 이걸로 하면 왜 안됨?????????????

# def prefix_sum(pad, sign=1):
#     global board_black, board_white

#     for y in range(pad, N):
#         board_black[y][pad - 1] = board_black[y][pad - 1] + (board_black[y - pad][pad - 1]) * sign
#         board_white[y][pad - 1] = board_white[y][pad - 1] + (board_white[y - pad][pad - 1]) * sign

#     for x in range(pad, M):
#         board_black[pad - 1][x] = board_black[pad - 1][x] + (board_black[pad - 1][x - pad]) * sign
#         board_white[pad - 1][x] = board_white[pad - 1][x] + (board_white[pad - 1][x - pad]) * sign

#     for y in range(pad, N):
#         for x in range(pad, M):
#             board_black[y][x] = board_black[y][x] + (board_black[y - pad][x] + board_black[y][x - pad] - board_black[y - pad][x - pad]) * sign
#             board_white[y][x] = board_white[y][x] + (board_white[y - pad][x] + board_white[y][x - pad] - board_white[y - pad][x - pad]) * sign

# prefix_sum(1)
# prefix_sum(K, sign=-1)