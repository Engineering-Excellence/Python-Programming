# [문제4] 다음 empList 변수는 '입사년도이름급여' 순으로 사원의 정보가 기록된 자료이다. 전체 사원 급여의 평균과 평균 이상 급여 수령자 목록을 출력하는 함수를 정의하시오.

from re import sub
from Pywork.chapter07.exercise import ex03


# 함수 정의
def pay_pro(emps: list[str]) -> None:
    """
    전체 사원 급여의 평균과 평균 이상 급여 수령자 목록을 출력하는 함수
    :param emps: 사원 정보
    :type emps: list[str]
    :return: None
    :rtype: None
    """
    avg_sal: int = ex03.pay_pro(emps)
    print('전체 급여 평균: %d' % avg_sal)
    print('평균 이상 급여 수령자')
    for emp in emps:
        name = sub('\\d', '', emp)
        sal = int(sub('\\d{4}[가-힣]+', '', emp))
        if sal >= avg_sal:
            print(f'{name} => {sal}')


if __name__ == '__main__':
    empList: list[str] = ['2014홍길동220', '2002이순신300', '2010유관순260']

    # 함수 호출
    pay_pro(empList)
