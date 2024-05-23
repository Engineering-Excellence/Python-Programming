# 4.5 알고리즘(Algorithm)

# 알고리즘: 문제를 해결하기 위한 일련의 절차
# 알고리즘의 조건: 입력, 출력, 명백성, 유한성, 효과성

# 4.5.1 최댓값/최솟값(max/min)
# (1) 입력 자료 생성
import random
dataset = []
for i in range(10):
    r = random.randint(1, 100)
    dataset.append(r)
print(dataset)

# (2) 변수 초기화
vmax = vmin = dataset[0]

# (3) 최댓값/최솟값 구하기
for i in dataset:
    if vmax < i:
        vmax = i
    if vmin > i:
        vmin = i

# (4) 결과 출력
print(f'max = {vmax}, min = {vmin}')

print()

# 4.5.2 정렬(sort)
# 선택 정렬: 첫 번째 원소를 기준으로 나머지 모든 원소를 비교하여 정렬
# (1) 오름차순 정렬
dataset = [3, 5, 1, 2, 4]
n = len(dataset)
for i in range(n - 1):
    for j in range(i + 1, n):
        if dataset[i] > dataset[j]:
            dataset[i], dataset[j] = dataset[j], dataset[i]
    print(dataset)  # 각 회전 정렬 내용
print(dataset)  # [1, 2, 3, 4, 5]

print()

# (2) 내림차순 정렬
dataset = [3, 5, 1, 2, 4]
for i in range(n - 1):
    for j in range(i + 1, n):
        if dataset[i] < dataset[j]:
            dataset[i], dataset[j] = dataset[j], dataset[i]
    print(dataset)
print(dataset)
