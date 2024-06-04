# 6.2 클래스 구성

# 6.2.1 함수와 클래스
from typing import Callable


# (1) 함수 정의
def calc_func(a: int, b: int) -> tuple[Callable, Callable]:
    # 변수 선언: 자료 저장
    x = a  # 10
    y = b  # 20

    def plus() -> int:  # 내부함수
        return x + y

    def minus() -> int:  # 내부함수
        return x - y

    return plus, minus


# (2) 함수 호출
p, m = calc_func(a=10, b=20)
print('plus =', p())
print('minus =', m())

print()


# (3) 클래스 정의
class CalcClass:
    # 클래스 변수: 자료 저장
    x = y = 0

    # 생성자: 객체 생성 + 멤버변수 초기화
    def __init__(self, a: int, b: int):
        self.x = a  # 10
        self.y = b  # 20

    # 클래스 함수
    def plus(self) -> int:
        return self.x + self.y

    # 클래스 함수
    def minus(self) -> int:
        return self.x - self.y


# (4) 객체 생성
obj = CalcClass(a=10, b=20)

# (5) 멤버 호출
print('plus =', obj.plus())
print('minus =', obj.minus())
