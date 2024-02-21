import sys
input = sys.stdin.readline

N = int(input()) # 타겟 채널
M = int(input()) # 고장난 채널 수

if M > 0:
    broken_buttons = list(map(int, input().split()))
else:
    broken_buttons = list()


'''
자리수를 가장 큰 자리수부터 순서대로 맞춤?
첫번째 자리수가 a1일 때, 고장나지 않은 숫자들 중 |a1-고장난 숫자|가 가장 작은 것을 뽑음.
최대 2가지 경우가 나올 수 있는데, 그럼 케이스를 나눠서 들어감.
최종적으로 만들어진 수 후보들 중 차의 절댓값이 가장 작은 것을 선택.

나눠서 들어가더라도 최대 6자리 수라서 2 ^ 6의 경우가 됨

100으로부터 시작한다는 점 고려

---

쌩 브루트 포스로 푸는 문제라고 함
'''

minimum = abs(100 - N)

for num in range(999999):
    str_num = str(num)

    for n in str_num:
        if int(n) in broken_buttons:
            break # 현재 탐색중인 num은 만들 수 없는 번호인 경우 다음 케이스로 넘어감
    
    # 만들 수 있는 번호 조합인 경우
    minimum = min(minimum, abs(N - num) + len(str_num))

print(minimum)