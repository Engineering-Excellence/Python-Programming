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
