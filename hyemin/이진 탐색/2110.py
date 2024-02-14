'''
'공유기 사이의 거리'를 이분 탐색으로 찾기

공유기 사이의 최소 거리 & 공유기 사이의 최대 거리를 바탕으로
그 절반을 공유기 사이의 초기 거리로 초기화해주고
그 거리를 기준으로 C보다 많이 설치할 수 있으면 거리를 늘려주고
C보다 적게 설치되면 거리차를 줄여주자
'''

N, C = map(int, input().split())

houses = []

for _ in range(N):
    houses.append(int(input()))

houses.sort()

start = 1 # 공유기 사이 최소 거리
end = houses[-1] - houses[0] # 공유기 사이 최대 거리

result = 0

while start <= end:
    mid = (start + end) // 2
    wifi = houses[0]
    cnt = 1

    for i in range(1, N):
        if houses[i] >= wifi + mid:
            cnt += 1
            wifi = houses[i]
    
    if cnt >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)