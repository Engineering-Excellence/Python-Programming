# 6.3.4 다형성
from typing_extensions import override


# (1) 부모 클래스
class Flight:
    # 부모 원형 함수
    def fly(self) -> None:
        print('날다, fly 원형 메서드')


# (2) 자식 클래스: 비행기
class Airplane(Flight):
    def __init__(self):
        super().__init__()

    # 함수 재정의
    @override
    def fly(self) -> None:
        print('비행기가 날다.')


# (2) 자식 클래스: 새
class Bird(Flight):
    def __init__(self):
        super().__init__()

    # 함수 재정의
    @override
    def fly(self) -> None:
        print('새가 날다.')


# (2) 자식 클래스: 종이비행기
class PaperAirplane(Flight):
    def __init__(self):
        super().__init__()

    # 함수 재정의
    @override
    def fly(self) -> None:
        print('종이비행기가 날다.')


# (3) 객체 생성
# 부모 객체 = 자식 객체(자식1, 자식2)
flight: Flight = Flight()  # 부모 클래스 객체
air: Airplane = Airplane()  # 자식1 클래스 객체
bird: Bird = Bird()  # 자식2 클래스 객체
paper: PaperAirplane = PaperAirplane()  # 자식3 클래스 객체

# (4) 다형성
flight.fly()  # 날다, fly 원형 메서드

flight = air
flight.fly()  # 비행기가 날다.

flight = bird
flight.fly()  # 새가 날다.

flight = paper
flight.fly()  # 종이비행기가 날다.
