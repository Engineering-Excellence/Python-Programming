# [문제1] Rectangle 클래스를 작성하시오.

from io import StringIO


class Rectangle:
    width: int = 0
    height: int = 0

    def __init__(self, width: int, height: int) -> None:
        """
        가로, 세로 멤버 변수 초기화
        :param width: 가로
        :type width: int
        :param height: 세로
        :type height: int
        """
        self.width = width
        self.height = height

    def area_calc(self) -> int:
        """
        사각형의 넓이를 구하는 함수
        :return: 가로 * 세로
        """
        return self.width * self.height

    def circum_calc(self) -> int:
        """
        사각형의 둘레를 구하는 함수
        :return: (가로 + 세로) * 2
        """
        return (self.width + self.height) * 2


if __name__ == '__main__':
    print("사각형의 넓이와 둘레를 계산합니다.")
    w = int(input("사각형의 가로 입력: "))
    h = int(input("사각형의 세로 입력: "))

    buffer = StringIO()
    buffer.write('-' * 30 + '\n')
    r: Rectangle = Rectangle(width=w, height=h)
    buffer.write(f"사각형의 넓이: {r.area_calc()}\n")
    buffer.write(f"사각형의 둘레: {r.circum_calc()}\n")
    buffer.write('-' * 30)
    print(buffer.getvalue())
    buffer.close()
