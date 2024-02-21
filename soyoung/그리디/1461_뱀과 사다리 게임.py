N,M=[*map(int,input().split())]
books=[*map(int,input().split())]
 
positive = []; negative = []; last = 0
for b in books:
    last = max(abs(b),last)
    if b>0:
        positive.append(b)
    else:
        negative.append(abs(b))
positive.sort(reverse = 1); negative.sort(reverse = 1)
 
result = 0
for i in range(0, len(positive), M):
    result += positive[i]*2
for i in range(0, len(negative), M):
    result += negative[i]*2
print(result-last)