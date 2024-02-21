import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N: 저장된 사이트 주소 수, M: 비밀 번호를 찾으려는 사이트 주소 수

all_data = {}

for i in range(N):
    url, password = map(str, input().split())
    all_data[url.strip()] = password.strip()

for i in range(M):
    target_url = input().strip()
    print(all_data[target_url])