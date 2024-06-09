# 6.3.2 상속
# (1) 부모 클래스
class Super:
    # 생성자: 동적멤버 생성
    def __init__(self, name: str, age: int) -> None:
        print('부모 클래스 생성자')
        self.__name = name
        self.__age = age

    # 메서드
    def display(self) -> None:
        print('name: %s, age: %d' % (self.__name, self.__age))


sup: Super = Super(name='부모', age=55)
sup.display()  # 부모 멤버 호출

print()


# (2) 자식 클래스
class Sub(Super):  # 클래스 상속
    __gender = None  # 자식 멤버

    # (3) 생성자
    def __init__(self, name: str, age: int, gender: str) -> None:
        # super().__init__(name, age)  # 부모 클래스 생성자 호출: Java와 다르게 자동 호출되지 않음
        print('자식 클래스 생성자')
        self.__name = name
        self.__age = age
        self.__gender = gender

    # (4) 메서드 확장
    def display(self) -> None:
        print('name: %s, age: %d, gender: %s' % (self.__name, self.__age, self.__gender))


sub: Sub = Sub(name='자식', age=25, gender='여자')
sub.display()  # 자식 멤버 호출
