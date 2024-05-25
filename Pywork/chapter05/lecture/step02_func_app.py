# 5.4.1 산포도 구하기
from statistics import mean, variance
from math import sqrt

dataset = [2, 4, 5, 6, 1, 8]


# (1) 산술평균
def Avg(data: list) -> float:
    avg = mean(data)
    return avg


print("산술평균 =", Avg(dataset))

print()


# (2) 분산/표준편차
def var_sd(data: list) -> tuple:
    avg = Avg(data)  # 함수 호출

    # list 내포
    diff = [(d - avg) ** 2 for d in data]

    var = sum(diff) / (len(data) - 1)
    sd = sqrt(var)

    return var, sd


# (3) 함수 호출
v, s = var_sd(dataset)
print("분산(사용자정의함수) =", v)
print("분산(내장함수) =", variance(dataset))
print("표준편차 =", s)

print()


# 5.4.2 피타고라스 정리
def pytha(s: int, t: int):
    a = s ** 2 - t ** 2
    b = 2 * s * t
    c = s ** 2 + t ** 2
    print(f'3변의 길이: {a}, {b}, {c}')


pytha(2, 1)  # s, t의 인수는 양의 정수를 갖는다.
