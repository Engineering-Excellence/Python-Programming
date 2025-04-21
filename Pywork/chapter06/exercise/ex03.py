# [문제3] Person 클래스를 작성하시오.

from io import StringIO
from logging import Logger, getLogger, Handler, StreamHandler, ERROR
from sys import stderr


class Person:
    name: str = ""
    age: int = 0
    gender: str = ""

    def __init__(self, name: str, age: int, gender: str) -> None:
        """
        생성자
        :param name: 이름
        :type name: str
        :param age: 나이
        :type age: int
        :param gender: 성별
        :type gender: str
        """
        self.name = name
        self.age = age
        self.gender = gender

    def display(self) -> None:
        """
        개인정보 출력
        :return: None
        """
        buffer: StringIO = StringIO()
        buffer.write('=' * 30 + '\n')
        buffer.write(f"이름: {self.name}, ")
        buffer.write(f"성별: {'여자' if self.gender == 'female' else '남자'}\n")
        buffer.write(f"나이: {self.age}\n")
        buffer.write('=' * 30)
        print(buffer.getvalue())
        buffer.close()


if __name__ == "__main__":
    # 키보드 입력
    logger: Logger = getLogger()
    handler: Handler = StreamHandler(stderr)
    logger.addHandler(handler)
    logger.setLevel(ERROR)

    userName: str = input("이름: ")
    try:
        userAge: int = int(input("나이: "))
    except ValueError:
        logger.error("숫자를 입력하세요.")
        exit(1)
    if userAge < 0:
        logger.error("음이 아닌 정수를 입력하세요.")
        exit(1)
    userGender: str = input("성별(male/female): ")
    if userGender not in ("male", "female"):
        logger.error("잘못된 성별입니다.")
        exit(1)

    person: Person = Person(name=userName, age=userAge, gender=userGender)
    person.display()
