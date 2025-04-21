# 7.2.2 문자열 검사

from re import match, Match


def is_jumin(res: Match[str]) -> None:
    """
    주민등록번호 일치 여부 출력 함수

    :param res: 주민등록번호에 match()를 적용한 결과
    :type res: Match[str]
    :return: None
    """
    print(res)
    if res:  # object
        print("주민번호 일치")
    else:  # None
        print("잘못된 주민번호")


# (1) 패턴과 일치된 경우
jumin: str = "123456-3234567"
result: Match[str] = match(pattern="[0-9]{6}-[1-4][0-9]{6}", string=jumin, flags=0)  # pattern: str이 내부적으로 compile 됨
is_jumin(result)
print()

# (2) 패턴과 불일치된 경우
jumin = "123456-5234567"
result = match("\\d{6}-[1-4]\\d{6}", jumin)
is_jumin(result)
