# [문제2] 동적 멤버 변수를 생성하여 산포도를 구하는 클래스를 정의하시오.

from statistics import mean
from math import sqrt


# 산포도 클래스
class Scattering:
    data: list[int] = list()

    def __init__(self, data: list[int]) -> None:
        """
        생성자
        :param data: 표본
        :type data: list[int]
        """
        self.data = data

    def var_func(self) -> float:
        """
        분산을 구하는 메서드
        :return: 분산
        """
        avg: float = mean(self.data)
        return sum([(d - avg) ** 2 for d in self.data]) / (len(self.data) - 1)

    def std_func(self) -> float:
        """
        표준편차를 구하는 메서드
        :return: 표준편차
        """
        return sqrt(self.var_func())


if __name__ == '__main__':
    x: list[int] = [5, 9, 1, 7, 4, 6]
    s: Scattering = Scattering(data=x)
    print(f"분산: {s.var_func()}")
    print(f"표준편차: {s.std_func()}")
