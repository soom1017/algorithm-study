## 정렬
메모리 제한 or 시간 제한에 걸릴 만한 탐색을 수행해야 할 때 "정렬 후" 이진탐색을 사용한다.

대표적인 정렬 방식은 다음과 같다.

|방식|시간복잡도|
|--|---|
|선택 정렬|$O(N^2)$|
|삽입 정렬|$O(N^2)$, 정렬된 상태에선 $O(N)$|
|퀵 정렬|$O(N \log N)$|
|계수 정렬|$O(N + K)$, &nbsp;&nbsp;&nbsp;&nbsp; $K$: 데이터 중 최댓값|
|파이썬 기본 정렬|$O(N \log N)$|

$O(N^2)$의 시간복잡도를 가지는 경우, $N = 1,000$이면 약 0.35초지만 $N = 10,000$이면 15초 넘게 걸리므로, <br/>이 경우 다른 정렬 알고리즘을 고려해야 한다.

### 선택 정렬
```python
for i in range(len(arr)):
    min_idx = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
```

### 삽입 정렬
```python
for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
        else:
            break
```

### 퀵 정렬
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    tail = arr[1:]
    
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
```

### 계수 정렬
범위가 제한된 (최솟값과 최댓값의 차이가 크지 않은), discrete한 데이터에 적합하다.

```python
count = [0] * (max(arr) + 1)

for i in range(len(arr)):
    count[arr[i]] += 1

# 이후 출력에서 K만큼 소요
```

## 이진 탐색
당연하게도 정렬된 상태에서만 사용 가능하다. 파이썬에는 `from bisect import bisect_left`로 가져올 수 있는 훌륭한 라이브러리 함수가 있지만, 혹시 손으로 구현하라 할 수 있으니 아래에 적어둔다..

재귀로도 구현할 수 있지만, 재귀 깊이가 깊어질 경우 stack overflow 에러가 날 수 있으니 반복문으로 외워둘 예정.

```python
def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return None

result = binary_search(arr, target, 0, n-1)
```

