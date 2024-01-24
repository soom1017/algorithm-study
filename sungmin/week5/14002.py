import sys, copy
input = sys.stdin.readline

N = int(input())
SEQ = list(map(int, input().split()))

DP = [1] * N
RET = [[i] for i in SEQ]
for i in range(N)[1:]:
    for j in range(i):
        if SEQ[i] > SEQ[j]:
            if DP[i] < DP[j] + 1:
                DP[i] = DP[j] + 1
                RET[i] = copy.deepcopy(RET[j])
                RET[i].append(SEQ[i])

print(max(DP))
for i in RET[DP.index(max(DP))]:
    print(i,end=' ')