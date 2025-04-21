# [문제4] Employee 클래스를 상속받아서 Permanent와 Temporary 클래스를 구현하시오.

from typing import Optional
from logging import Logger, getLogger, StreamHandler, ERROR
from io import StringIO


# 부모클래스
class Employee:
    etype: Optional[str] = None
    name: Optional[str] = None
    pay: Optional[int] = None

    def __init__(self, etype: str, name: str) -> None:
        """
        부모클래스 생성자

        :param etype: 고용형태
        :type etype: str
        :param name: 이름
        :type name: str
        """
        self.etype = "정규직" if etype == 'P' else '임시직'
        self.name = name


# 자식클래스 - 정규직
class Permanent(Employee):
    bpay: Optional[int] = None
    bonus: Optional[int] = None

    def __init__(self, etype: str, name: str, bpay: int, bonus: int) -> None:
        """
        정규직 생성자

        :param etype: 고용형태
        :type etype: str
        :param name: 이름
        :type name: str
        :param bpay: 기본급
        :type bpay: int
        :param bonus: 상여금
        :type bonus: int
        """
        super().__init__(etype, name)
        self.bpay = bpay
        self.bonus = bonus
        self.pay = bpay + bonus


# 자식클래스 - 임시직
class Temporary(Employee):
    turnaround: Optional[int] = None
    tpay: Optional[int] = None

    def __init__(self, etype: str, name: str, turnaround: int, tpay: int) -> None:
        """
        임시직 생성자

        :param etype: 고용형태
        :type etype: str
        :param name: 이름
        :type name: str
        :param turnaround: 작업시간
        :type turnaround: int
        :param tpay: 시급
        :type tpay: int
        """
        super().__init__(etype, name)
        self.turnaround = turnaround
        self.tpay = tpay
        self.pay = tpay * turnaround


if __name__ == "__main__":
    logger: Logger = getLogger()
    logger.addHandler(StreamHandler())
    logger.setLevel(ERROR)

    employee: Optional[Employee] = None
    try:
        empType: str = input("고용형태 선택(정규직<P>, 임시직<T>): ")
        if empType.upper() == "P":  # 정규직
            empName: str = input("이름: ")
            empBpay: int = int(input("기본급: "))
            bns: int = int(input("상여금: "))
            employee = Permanent(etype=empType, name=empName, bpay=empBpay, bonus=bns)
        elif empType.upper() == "T":  # 임시직
            empName: str = input("이름: ")
            ta: int = int(input("작업시간: "))
            tp: int = int(input("시급: "))
            employee = Temporary(etype=empType, name=empName, turnaround=ta, tpay=tp)
        else:  # 고용형태 입력 오류
            print('=' * 30)
            logger.error('입력 오류')
            exit(1)
    except ValueError:
        print('=' * 30)
        logger.error("숫자를 입력하세요.")
        exit(1)

    buffer = StringIO()
    buffer.write('=' * 30 + '\n')
    buffer.write(f"고용형태: {employee.etype}\n")
    buffer.write(f"이름: {employee.name}\n")
    buffer.write(f"급여: {employee.pay:,}")
    print(buffer.getvalue())
    buffer.close()
