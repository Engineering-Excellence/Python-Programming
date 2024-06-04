# [문제2] 중첩함수를 적용하여 은행계좌 함수를 작성하시오.

# 함수 정의
def bank_account(bal: int) -> tuple:
    balance = bal  # 잔액 초기화(1000)

    def get_balance() -> int:  # 잔액확인(getter)
        return balance

    def deposit(money: int) -> None:  # 입금하기(setter)
        nonlocal balance
        balance += money

    def withdraw(money: int) -> None:  # 출금하기(setter)
        nonlocal balance
        balance -= money

    return get_balance, deposit, withdraw  # 클로저 함수 리턴


b, d, w = bank_account(bal=int(input('최초 계좌의 잔액을 입력하세요.: ')))
print(f'현재 계좌 잔액은 {b()}원입니다.')
d_money = int(input('입금액을 입력하세요.: '))
d(money=d_money)
print(f'{d_money}원 입금 후 잔액은 {b()}원입니다.')
w_money = int(input('출금액을 입력하세요.: '))
w(money=w_money)
print(f'{w_money}원 출금 후 잔액은 {b()}원입니다.')
