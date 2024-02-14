'''
진실을 알고 있는 사람: known_list
각 파티 참석자: party_list
파티 목록: parties

1. party_list와 known_list가 하나라도 겹치면(두 집합의 union != null) 해당 party_list를 know_list와 합쳐줌(known_list = union(known_list, party_list))
2. 1번 연산을 parties의 모든 party 원소에 대해 수행
3. 다시 parties를 순회하면서 known_list와 party_list 간의 교집합이 있는지 확인
'''

N, M = map(int, input().split())
known_list = set(input().split()[1:])
parties = []

for _ in range(M):
    parties.append(set(input().split()[1:]))

for _ in range(M):
    for party in parties:
        if party & known_list:
            known_list = known_list.union(party)

cnt = 0

for party in parties:
    if party & known_list:
        continue
    else:
        cnt += 1

print(cnt)