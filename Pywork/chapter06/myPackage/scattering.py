# 6.5 패키지와 모듈

# 6.5.1 라이브러리 import

# (1) 평균과 제곱근 모듈 import
from statistics import mean
from math import sqrt


# (2) 산술평균 함수
def avg(data) -> float:
    return mean(data)


# (3) 분산/표준편차 함수
def var_sd(data) -> tuple[float, float]:  # [2, 4, 5, 6, 1, 8] - avg
    average: float = avg(data)  # 함수 호출
    diff: list[float] = [(d - average) ** 2 for d in data]  # list 내포
    var: float = sum(diff) / (len(data) - 1)
    sd: float = sqrt(var)
    return var, sd
