N, M = map(int, input().split())
truth = set(list(map(int, input().split()))[1:])

parties = []
for _ in range(M):
    parties.append(set(list(map(int, input().split()))[1:]))

for _ in range(M):
    for party in parties:
        if party & truth:
            truth = truth.union(party)

count = 0
for party in parties:
    if party & truth: continue
    count += 1

print(count)