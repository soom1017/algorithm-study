import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
btn = list(map(int,input().split()))

# 100번에서 한칸씩 이동
ans = abs(n-100)

# 숫자 버튼 입력 -> 한칸씩 이동
for i in range(1000001):
    i = str(i)
    for j in i:
        if int(j) in btn:
            break
    # 1차적으로 가려는 채널 숫자 버튼이 모두 고장나지 않았으면
    else:
        # 숫자 버튼을 누르는 횟수 + 한칸씩 이동하는 횟수
        ans = min(ans, len(i)+abs(int(i)-n))
print(ans)