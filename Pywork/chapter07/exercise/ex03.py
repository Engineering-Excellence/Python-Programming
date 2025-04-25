# [문제3] 다음 empList 변수는 '입사년도이름급여' 순으로 사원의 정보가 기록된 자료이다. empList 변수를 이용하여 전체 사원 급여의 평균을 구하는 함수를 정의하시오.

from re import sub, compile, Pattern
from statistics import mean


# 함수 정의
def pay_pro(emps: list[str]) -> int:
    """
    급여 평균 계산 함수

    :param emps: 사원정보
    :type emps: list[str]
    :return: 사원 급여 평균
    :rtype: float
    """
    pat: Pattern[str] = compile('\\d{4}[가-힣]+')
    return mean([int(sub(pat, '', emp)) for emp in emps])


if __name__ == '__main__':
    empList: list[str] = ['2014홍길동220', '2002이순신300', '2010유관순260']

    # 함수 호출
    pays_mean: int = pay_pro(empList)
    print('전체 사원 급여 평균: %d' % pays_mean)
