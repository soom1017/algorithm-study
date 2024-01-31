# 15652

N, M = map(int, input().split())
sequence = []

def back_tracking(idx):
    if len(sequence) == M:
        print(" ".join(map(str, sequence)))
        return
    
    for i in range(idx, N + 1):
        sequence.append(i)
        back_tracking(i)
        sequence.pop()

back_tracking(1)