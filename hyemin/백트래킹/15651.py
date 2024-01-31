# 15651

N, M = map(int, input().split())
sequence = []

def back_tracking():
    if len(sequence) == M:
        print(" ".join(map(str, sequence)))
        return
    
    for i in range(1, N + 1):
        sequence.append(i)
        back_tracking()
        sequence.pop()

back_tracking()