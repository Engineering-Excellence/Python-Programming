# 6.5 패키지와 모듈

# 6.5.1 라이브러리 import

# (1) 평균과 제곱근 모듈 import
from statistics import mean
from math import sqrt


# (2) 산술평균 함수
def average(data) -> float:
    return mean(data)


# (3) 분산/표준편차 함수
def var_sd(data) -> tuple[float, float]:  # [2, 4, 5, 6, 1, 8] - avg
    avg: float = average(data)  # 함수 호출
    ss: list[float] = [(d - avg) ** 2 for d in data]  # list 내포
    var: float = sum(ss) / (len(data) - 1)
    sd: float = sqrt(var)
    return var, sd


# 6.5.2 시작점(main) 만들기

# 프로그램 시작점
if __name__ == '__main__':
    sample: range = range(1, 8, 2)
    print(f'평균 = {average(sample)}')
    variance, deviation = var_sd(sample)
    print(f'분산 = {variance}')
    print(f'표준편차 = {deviation}')
