# 6.2.3 생성자

# (1) 생성자 이용 멤버변수 초기화
class Multiply:
    # 멤버 변수
    x = y = 0

    # 생성자: 초기화
    def __init__(self, x: int, y: int) -> None:  # 객체만 생성
        self.x = x
        self.y = y

    # 메서드
    def mul(self) -> int:
        return self.x * self.y


obj: Multiply = Multiply(x=10, y=20)  # 생성자
print('곱셈 =', obj.mul())


# (2) 메서드 이용 멤버변수 초기화
class Multiply2:
    # 멤버 변수
    x = y = 0

    # 생성자 없음: 기본 생성자 제공

    # 메서드: 멤버변수 초기화
    def data(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    # 메서드: 곱셈
    def mul(self) -> int:
        return self.x * self.y

    # 소멸자: 객체 소멸
    def __del__(self) -> None:
        del self.x
        del self.y


obj: Multiply2 = Multiply2()  # 기본 생성자
obj.data(x=10, y=20)  # 동적 멤버변수 생성
print('곱셈 =', obj.mul())

print()


# 6.2.4 self
class Multiply3:
    # 멤버변수 없음
    # 생성자 없음

    # 동적 멤버변수 생성/초기화
    def data(self, x: int, y: int) -> None:
        self.x = x  # 호출시 동적으로 멤버변수 생성
        self.y = y

    # 곱셈 연산
    def mul(self) -> None:
        self.display(self.x * self.y)

    # 결과 출력
    def display(self, result: int) -> None:
        print('곱셈 = %d' % result)


obj: Multiply3 = Multiply3()  # 기본 생성자
obj.data(x=10, y=20)
obj.mul()
