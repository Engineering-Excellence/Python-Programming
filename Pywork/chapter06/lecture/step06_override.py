# 6.3.3 메서드 재정의

# (1) 부모클래스
from typing import Optional


class Employee:
    name: str = Optional[str]
    pay: int = 0

    def __init__(self, name: str) -> None:
        self.name = name

    def pay_calc(self, var1: int, var2: int) -> None:
        pass


# (2) 자식클래스: 정규직
class Permanent(Employee):
    def __init__(self, name: str) -> None:
        super().__init__(name)  # 부모 생성자 호출

    def pay_calc(self, base: int, bonus: int) -> None:
        self.pay = base + bonus  # 급여=기본급+상여금
        print('총 수령액:', format(self.pay, '3,d'), '원')


# (3) 자식클래스: 임시직
class Temporary(Employee):
    def __init__(self, name: str) -> None:
        super().__init__(name)  # 부모 생성자 호출

    def pay_calc(self, tpay: int, time: int) -> None:
        self.pay = tpay * time  # 급여=작업시간*시급
        print(f'총 수령액: {self.pay:3,d} 원')


# (4) 객체 생성
p: Permanent = Permanent("이순신")
p.pay_calc(base=3000000, bonus=200000)

t: Temporary = Temporary("홍길동")
t.pay_calc(tpay=15000, time=80)
