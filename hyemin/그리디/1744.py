import sys
input = sys.stdin.readline

seq_pos = []
seq_one = []
seq_zero = []
seq_neg = []

N = int(input())

sum_result = 0

for _ in range(N):
    num = int(input())
    if num > 1:
        seq_pos.append(num)
    elif num == 1:
        sum_result += 1
    elif num == 0:
        seq_zero.append(num)
    else:
        seq_neg.append(num)

seq_pos.sort(reverse=True)
seq_neg.sort()


if len(seq_pos) % 2 != 0:
    sum_result += seq_pos.pop()

for i in range(0, len(seq_pos) - 1, 2):
    sum_result += seq_pos[i] * seq_pos[i+1]

if len(seq_neg) % 2 != 0:
    neg_num = seq_neg.pop()
    if len(seq_zero) == 0: # 수열에 0이 있는 경우 (음수 * 0)을 연산하여 음수를 더하지 않을 수 있다.
        sum_result += neg_num

for i in range(0, len(seq_neg) - 1, 2):
    sum_result += seq_neg[i] * seq_neg[i+1] # 음수 * 음수 = 양수

print(sum_result)