# 15650

N, M = map(int, input().split())
sequence = []

def back_tracking(idx):
    if len(sequence) == M:
        print(" ".join(map(str, sequence)))
        return
    
    for i in range(idx, N + 1):
        if i not in sequence:
            sequence.append(i)
            back_tracking(i + 1)
            sequence.pop()

back_tracking(1)