# 배: https://acmicpc.net/problem/1092
n = int(input())
crains = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

crains.sort(reverse=True)
boxes.sort(reverse=True)

count = 0
if boxes[0] > crains[0]:
    print(-1)
else:
    while boxes:
        for crain in crains:
            for i in range(len(boxes)):
                if boxes[i] <= crain:
                    del boxes[i]
                    break
        count += 1
    print(count)