# 5.6 중첩함수
from typing import Callable


# 5.6.1 일급 함수와 함수 클로저
# (1) 일급 함수: 함수를 객체로 만들어서 사용하는 함수. 외부함수나 내부함수를 변수에 저장할 수 있는 특성을 가짐.
def a() -> Callable[[], None]:  # outer
    print('a 함수')

    def b() -> None:  # inner
        print('b 함수')

    return b


c = a()  # 외부 함수 호출: a 함수
c()  # 내부 함수 호출: b 함수

print()

# (2) 함수 클로저
data = list(range(1, 101))


def outer_func(data: list) -> tuple[Callable[[], int], Callable[[int], float]]:
    dataSet = data  # 값(1~100) 생성

    # inner
    def total() -> int:
        return sum(dataSet)

    def average(tot_val: int) -> float:
        return tot_val / len(dataSet)

    return total, average  # inner 반환


# 외부 함수 호출: data 생성
tot, avg = outer_func(data=data)

# 내부 함수 호출
tot_val = tot()
print('tot =', tot_val)
avg_val = avg(tot_val)
print('avg =', avg_val)

print()

# 5.6.2 중첩함수 역할
# 외부 함수: 함수에서 사용할 자료를 만들고, 내부 함수를 포함하는 역할을 한다.
# 내부 함수: 외부 함수에서 만든 자료를 연산하고 조작하는 역할을 한다.

from math import sqrt
from statistics import mean

data = [4, 5, 3.5, 2.5, 6.3, 5.5]


# (1) 외부 함수: 산포도 함수
def scattering_func(data: list) -> tuple[Callable, Callable, Callable]:  # outer
    dataSet = data  # data 생성

    # (2) 내부 함수: 산술평균 반환
    def avg_func() -> float:
        avg_val = mean(dataSet)
        return avg_val

    # (3) 내부 함수: 분산 반환
    def var_func(avg: float) -> float:
        diff = [(data - avg) ** 2 for data in dataSet]
        # print(sum(diff))  # 차의 합
        var_val = sum(diff) / (len(dataSet) - 1)
        return var_val

    # (4) 내부 함수: 표준편차 반환
    def std_func(var: float) -> float:
        std_val = sqrt(var)
        return std_val

    # 함수 클로저 반환
    return avg_func, var_func, std_func


# (5) 외부 함수 호출
avg, var, std = scattering_func(data=data)

# (6) 내부 함수 호출
print('평균:', avg())
print('분산:', var(avg()))
print('표준편차:', std(var(avg())))

print()


# 5.6.3 획득자(Getter), 지정자(Setter), nonlocal
# 획득자: 함수 내부에서 생성한 자료를 외부로 반환하는 함수로 반드시 return 명령문을 갖는다.
# 지정자: 함수 내부에서 생성한 자료를 외부에서 수정하는 함수로 반드시 매개변수를 갖는다. 만약 외부 함수에서 생성된 자료를 수정할 경우에는 해당 변수에 nonlocal 명령어를 쓴다.

# (1) 중첩함수 정의
def main_func(num: int) -> tuple[Callable[[], int], Callable[[int], None]]:
    num_val = num  # 자료 생성

    def getter() -> int:  # 획득자 함수, return 있음
        return num_val

    def setter(value: int) -> None:  # 지정자 함수, 인수 있음
        nonlocal num_val  # nonlocal 명령어
        num_val = value

    return getter, setter  # 함수 클로저 반환


# (2) 외부 함수 호출
getter, setter = main_func(num=100)  # num 생성

# (3) 획득자 호출
print('num =', getter())  # 획득한 num 확인

# (4) 지정자 획득
setter(200)  # num 값 수정
print('num =', getter())  # num 수정 확인

print()


# 5.6.4 함수 장식자(Decoration)
# (1) 래퍼 함수
def wrap(func: Callable[[], None]):
    def decorated() -> None:
        print('반가워요!')  # 시작 부분에 삽입
        func()  # 인수로 넘어온 함수(hello)
        print('잘 가요!')  # 종료 부분에 삽입

    return decorated  # 클로저 함수 반환


# (2) 함수 장식자 적용
@wrap
def hello() -> None:
    print('Hi~', '홍길동')


# (3) 함수 호출
hello()

print()


# 5.7 재귀함수

# 5.7.1 카운트
# (1) 재귀함수 정의: 1~n 카운트
def counter(n: int) -> int:
    if n == 0:
        return 0  # 종료 조건
    else:
        counter(n - 1)  # 재귀호출
        print(n, end=' ')


# (2) 함수 호출1
print('n = 0:', counter(n=0))

# (3) 함수 호출2
counter(n=5)
