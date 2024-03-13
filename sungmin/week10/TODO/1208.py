N, S = map(int, input().split())
ARR = list(map(int, input().split()))

left_array = ARR[:N//2]
right_array = ARR[N//2:]

def subseq(array):
    sub = []
    for i in array:
        _sub = sub[:]
        sub.append(i)
        for v in _sub: sub.append(v * i)
    return sorted(sub)

left_seq = subseq(left_array)
right_seq = subseq(right_array)
