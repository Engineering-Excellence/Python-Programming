# 6.3 객체지향 기법

# 6.3.1 캡슐화
class Account:
    # (1) 은닉 멤버변수
    __balance: int = 0  # 잔액
    __acc_name = None  # 예금주
    __acc_no = None  # 계좌번호

    # (2) 생성자: 멤버변수 초기화
    def __init__(self, balance: int, name: str, no: str) -> None:
        self.__balance = balance  # 잔액 초기화
        self.__acc_name = name  # 예금주 초기화
        self.__acc_no = no  # 계좌번호 초기화

    # (3) 계좌정보 확인: Getter
    def get_balance(self) -> tuple[int, str, str]:
        return self.__balance, self.__acc_name, self.__acc_no

    # (4) 입금하기: Setter
    def deposit(self, money: int) -> None:
        if money < 0:
            print('금액 확인')
            return  # 종료(exit)
        self.__balance += money

    # (5) 출금하기: Setter
    def withdraw(self, money: int) -> None:
        if self.__balance < money:
            print('잔액 부족')
            return  # 종료(exit)
        self.__balance -= money


# (6) object 생성
acc: Account = Account(balance=1000, name='홍길동', no='125-152-4125-41')  # 생성자

# (7) Getter 호출
# acc.__balance   # AttributeError
bal: tuple[int, str, str] = acc.get_balance()
print('계좌정보:', bal)

# (8) Setter 호출
acc.deposit(money=10000)  # 10000원 입금
bal = acc.get_balance()
print('계좌정보:', bal)  # 입금 확인
