# 6.2 클래스 구성

# 6.2.1 함수와 클래스
from typing import Callable


# (1) 함수 정의
def calc_func(a: int, b: int) -> tuple[Callable, Callable]:
    # 변수 선언: 자료 저장
    x: int = a  # 10
    y: int = b  # 20

    def plus() -> int:  # 내부함수
        return x + y

    def minus() -> int:  # 내부함수
        return x - y

    return plus, minus


# (2) 함수 호출
p, m = calc_func(a=10, b=20)
print('plus =', p())
print('minus =', m())


# (3) 클래스 정의
class CalcClass:
    # 클래스 변수: 자료 저장
    x = y = 0

    # 생성자: 객체 생성 + 멤버변수 초기화
    def __init__(self, a: int, b: int) -> None:
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

print()


# 6.2.2 클래스 구성 요소
class Car:
    # (1) 멤버변수
    cc: int = 0  # 엔진 cc
    door: int = 0  # 문짝 개수
    car_type = None  # null

    # (2) 생성자(초기자)
    def __init__(self, cc: int, door: int, car_type: str) -> None:
        # 멤버변수 초기화
        self.cc = cc
        self.door = door
        self.car_type = car_type  # 승용차, SUV

    # (3) 메서드
    def display(self) -> None:
        print('자동차는 %dcc이고, 문짝은 %d개, 타입은 %s.' % (self.cc, self.door, self.car_type))


# (4) 객체 생성
car1 = Car(cc=2000, door=4, car_type='승용차')  # 객체 생성 + 초기화
car2 = Car(cc=3000, door=5, car_type='SUV')

# (5) 멤버 호출: object.member()
car1.display()  # car1 멤버 호출
car2.display()  # car2 멤버 호출
