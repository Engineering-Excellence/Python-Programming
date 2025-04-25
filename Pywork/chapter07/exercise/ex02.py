# [문제2] 다음 empList 변수는 '입사년도이름급여' 순으로 사원의 정보가 기록된 자료이다. empList 변수를 이용하여 사원의 이름만 추출하는 함수를 정의하시오.

from re import sub


# 함수 정의
def name_pro(emps: list[str]) -> list[str]:
    """
    사원명 추출 함수

    :param emps: 사원정보
    :type emps: list[str]
    :return: 사원명단
    :rtype: list[str]
    """
    return [sub('\\d', '', emp) for emp in emps]


if __name__ == '__main__':
    empList: list[str] = ['2014홍길동220', '2002이순신300', '2010유관순260']

    # 함수 호출
    names: list[str] = name_pro(empList)
    print('names =', names)
